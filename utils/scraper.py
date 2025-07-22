import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_table():
    url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find("table", {"class": "wikitable"})
    df = pd.read_html(str(table))[0]
    df["Worldwide gross"] = df["Worldwide gross"].replace('[\$,]', '', regex=True).astype(float)
    df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
    return df
