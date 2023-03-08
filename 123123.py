import requests
from bs4 import BeautifulSoup

url = "https://bank.gov.ua/ua/markets/exchangerates"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"id": "exchangeRates"})
usd_rate = table.find("td", {"data-currency-code": "USD"}).text.strip()

print("Курс долара США: " + usd_rate)