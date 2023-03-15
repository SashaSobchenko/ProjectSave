import sqlite3

conn = sqlite3.connect('weather.db')
c = conn.cursor()

#c.execute('''CREATE TABLE weather
             #(date text, time text, temperature real)''')

conn.commit()
conn.close()
import sqlite3
import requests
from bs4 import BeautifulSoup
import datetime


conn = sqlite3.connect('weather.db')
c = conn.cursor()
#c.execute('''CREATE TABLE weather
             #(date text, time text, temperature real)''')
conn.commit()
conn.close()


page = requests.get("https://www.meteoprog.ua/uk/weather/Kyiv/")
soup = BeautifulSoup(page.content, 'html.parser')
temperature_elem = soup.find(class_='current-temp')
