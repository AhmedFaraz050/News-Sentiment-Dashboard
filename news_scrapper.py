# (Your scraping code)
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.dawn.com/latest-news'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='story')

headlines = []
for article in articles:
    headline = article.find('h2').text.strip()
    headlines.append(headline)

df = pd.DataFrame(headlines, columns=['Headline'])
df.to_csv("news_headlines.csv", index=False)

print("✅ Scraped", len(headlines), "headlines.")


# (Now add sentiment code)
from textblob import TextBlob

df['Sentiment_Score'] = df['Headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['Sentiment_Label'] = df['Sentiment_Score'].apply(
    lambda s: 'Positive' if s > 0 else ('Negative' if s < 0 else 'Neutral')
)

df.to_csv("news_sentiment.csv", index=False)
print("✅ Sentiment analysis complete. Saved to news_sentiment.csv")
print(df.head())
