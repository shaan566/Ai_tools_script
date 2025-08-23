from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import os

# ---------- Setup ----------
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ---------- CSV ----------
csv_filename = "futurepedia_tools_all.csv"
file = open(csv_filename, "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Name", "Link", "Image"])  # Header

# ---------- List of URLs ----------
urls = [
    'https://www.futurepedia.io/ai-tools/personal-assistant',
    'https://www.futurepedia.io/ai-tools/research-assistant',
    'https://www.futurepedia.io/ai-tools/spreadsheet-assistant',
    'https://www.futurepedia.io/ai-tools/translators',
    'https://www.futurepedia.io/ai-tools/presentations',
    'https://www.futurepedia.io/ai-tools/productivity',
    'https://www.futurepedia.io/ai-tools/video-enhancer',
    'https://www.futurepedia.io/ai-tools/video-editing',
    'https://www.futurepedia.io/ai-tools/video-generators',
    'https://www.futurepedia.io/ai-tools/text-to-video',
    'https://www.futurepedia.io/ai-tools/video',
    'https://www.futurepedia.io/ai-tools/prompt-generators',
    'https://www.futurepedia.io/ai-tools/writing-generators',
    'https://www.futurepedia.io/ai-tools/paraphrasing',
    'https://www.futurepedia.io/ai-tools/storyteller',
    'https://www.futurepedia.io/ai-tools/copywriting-assistant',
    'https://www.futurepedia.io/ai-tools/text-generators',
    'https://www.futurepedia.io/ai-tools/website-builders',
    'https://www.futurepedia.io/ai-tools/marketing',
    'https://www.futurepedia.io/ai-tools/finance',
    'https://www.futurepedia.io/ai-tools/project-management',
    'https://www.futurepedia.io/ai-tools/social-media',
    'https://www.futurepedia.io/ai-tools/business',
    'https://www.futurepedia.io/ai-tools/design-generators',
    'https://www.futurepedia.io/ai-tools/image-generators',
    'https://www.futurepedia.io/ai-tools/image-editing',
    'https://www.futurepedia.io/ai-tools/text-to-image',
    'https://www.futurepedia.io/ai-tools/image',
    'https://www.futurepedia.io/ai-tools/workflows',
    'https://www.futurepedia.io/ai-tools/ai-agents',
    'https://www.futurepedia.io/ai-tools/automations',
    'https://www.futurepedia.io/ai-tools/cartoon-generators',
    'https://www.futurepedia.io/ai-tools/portrait-generators',
    'https://www.futurepedia.io/ai-tools/avatar-generator',
    'https://www.futurepedia.io/ai-tools/logo-generator',
    'https://www.futurepedia.io/ai-tools/3D-generator',
    'https://www.futurepedia.io/ai-tools/art',
    'https://www.futurepedia.io/ai-tools/audio-editing',
    'https://www.futurepedia.io/ai-tools/text-to-speech',
    'https://www.futurepedia.io/ai-tools/music-generator',
    'https://www.futurepedia.io/ai-tools/transcriber',
    'https://www.futurepedia.io/ai-tools/audio-generators',
    'https://www.futurepedia.io/ai-tools/fitness',
    'https://www.futurepedia.io/ai-tools/religion',
    'https://www.futurepedia.io/ai-tools/students',
    'https://www.futurepedia.io/ai-tools/fashion-assistant',
    'https://www.futurepedia.io/ai-tools/gift-ideas',
    'https://www.futurepedia.io/ai-tools/misc-tools',
    'https://www.futurepedia.io/ai-tools/code-assistant',
    'https://www.futurepedia.io/ai-tools/no-code',
    'https://www.futurepedia.io/ai-tools/sql-assistant',
    'https://www.futurepedia.io/ai-tools/code'
]



def write_unique_tools(csv_filename, tools_data):
    """
    tools_data: list of tuples/lists like [(name, link, img), ...]
    Only adds new tools to CSV (based on link).
    """
    # Load existing links
    existing_links = set()
    if os.path.exists(csv_filename):
        with open(csv_filename, "r", newline="", encoding="utf-8") as f: # read mode only 
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 1:  # ensure there is a link column
                    existing_links.add(row[1])

   # Open CSV in append mode to add new entries
    with open(csv_filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for name, link, img in tools_data:
            if link not in existing_links:
                writer.writerow([name, link, img])
                existing_links.add(link)
                print("💾 Saved:", name)
            else:
                print("⏭ Skipping existing tool:", name)

# ---------- Scraper Function ----------
def scrape_tools_on_page():
    # Scroll to bottom to trigger lazy-loading images
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    tools = driver.find_elements(
        By.CSS_SELECTOR,
        "div.grid.w-full.grid-cols-1.grid-rows-3.gap-4.md\\:grid-cols-2.lg\\:grid-cols-3.lg\\:gap-6.xl\\:grid-cols-4.xl\\:gap-3 > div"
    )
    print(f"📄 Found {len(tools)} tools on this page")

    for tool in tools:
        # Scroll each tool into view
        driver.execute_script("arguments[0].scrollIntoView(true);", tool)
        time.sleep(0.3)

        # Tool Name
        try:
            name = tool.find_element(By.CSS_SELECTOR, "p").text.strip()
        except:
            name = ""

        # Tool Link
        try:
            link = tool.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        except:
            link = ""

        # Tool Image
        try:
            img_el = tool.find_element(By.TAG_NAME, "img")
            img = img_el.get_attribute("src") or img_el.get_attribute("data-src")
        except:
            img = ""

        writer.writerow([name, link, img])
        print("💾 Saved:", name)

# ---------- Loop through all URLs and paginate ----------
for url in urls:
    driver.get(url)
    time.sleep(3)
    page = 1
    while True:
        print(f"\n📄 Scraping {url} - Page {page}")
        scrape_tools_on_page()

        # Try to click next button
        try:
            next_btn = driver.find_element(
                By.CSS_SELECTOR,
                "div.flex.items-center.justify-center.py-12 > div > div > div > a:last-child"
            )
            if "pointer-events-none" in next_btn.get_attribute("class"):
                print("🎉 Last page reached!")
                break
            else:
                print("➡️ Clicking Next Page...")
                driver.execute_script("arguments[0].click();", next_btn)
                time.sleep(3)
                page += 1
        except:
            print("⚡ No Next button found, stopping pagination.")
            break

# ---------- Cleanup ----------
file.close()
driver.quit()
print("✅ All scraping completed! Data saved in", csv_filename)
