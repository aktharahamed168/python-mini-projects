import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    url = "https://quotes.toscrape.com/"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve webpage.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")

    print("===== Web Scraper =====")

    print("\nQuotes Found")
    print("------------")

    for number, quote in enumerate(quotes, start=1):
        print(f"{number}. {quote.text}")


scrape_quotes()
