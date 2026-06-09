import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        quotes_data.append({
            "Quote": text,
            "Author": author
        })

    df = pd.DataFrame(quotes_data)

    df.to_csv("quotes.csv", index=False)

    print("Scraping completed!")
    print(df.head())

else:
    print("Failed to fetch website")