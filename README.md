🛠️ Tools Scraper
📌 Description

Tools Scraper is a Python-based web scraper built using Selenium.
It automatically extracts AI tool details (like name, category, description, link) from Futurepedia
 (or any similar AI tools directory) and saves them into a CSV file.

This project is helpful if you want to:

Collect updated AI tools data weekly

Build your own AI tools directory

Perform SEO or competitor research on tools

🚀 Features

Scrapes tool name, description, link, category

Handles dynamic JavaScript-loaded content with Selenium

Saves data into a structured CSV file (futurepedia_tools_all.csv)

Can be automated to run weekly

📦 Requirements

Make sure you have the following installed:

Python 3.8+

Google Chrome (latest version)

ChromeDriver (auto-installed via webdriver-manager)

Install dependencies:

pip install selenium webdriver-manager

⚡ Usage

Clone the repository

git clone https://github.com/your-username/tools-scraper.git
cd tools-scraper


Run the scraper

python main.py


Output
A file named futurepedia_tools_all.csv will be created in the project folder.

📊 Example Output
Tool Name	Category	Link	Description
ChatGPT	AI Chat	https://chat.openai.com
	Conversational AI tool
Jasper	Copywriting	https://jasper.ai
	AI content generator
⏰ Automation

You can schedule this scraper to run every week:



Create a new task → Set trigger = weekly → Action = run python scraper.py

🔹 Cloud Options

GitHub Actions (free automation)

AWS Lambda / Google Cloud Functions
