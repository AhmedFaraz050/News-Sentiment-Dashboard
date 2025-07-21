# 📰 News Sentiment Analysis Dashboard

This project scrapes the latest news headlines from [Dawn.com](https://www.dawn.com/latest-news), analyzes their sentiment using Natural Language Processing (NLP), and visualizes the results in an interactive Power BI dashboard.

## 📌 Project Overview

- Scrape real-time headlines using `requests` and `BeautifulSoup`
- Analyze sentiment polarity with `TextBlob`
- Classify headlines into **Positive**, **Negative**, or **Neutral**
- Export the processed data to CSV
- Visualize insights in Power BI with:
  - KPI cards (total headlines, average sentiment)
  - Pie chart (sentiment distribution)
  - Bar chart (headline count by sentiment)
  - Interactive slicer
  - Summary and clean layout

## 🛠️ Tools & Technologies

- Python 3
- BeautifulSoup (web scraping)
- TextBlob (sentiment analysis)
- Pandas (data manipulation)
- Power BI (data visualization)

## 📂 Files Included

- `news_scraper.py` – Python script to scrape, analyze, and export data
- `news_sentiment.csv` – Final dataset used for visualization
- `news_headlines.csv` – Raw scraped headlines
- `dashboard.pbix` – *(optional)* Power BI dashboard file
- `README.md` – Project documentation

## 🚀 How to Run

1. Clone this repository  
2. Install required packages:  
   ```bash
   pip install requests beautifulsoup4 pandas textblob
   python -m textblob.download_corpora
