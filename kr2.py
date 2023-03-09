import requests
from bs4 import BeautifulSoup

search_text = input("Введите текст для поиска: ")

urls = [
    "https://ru.wikipedia.org/wiki/%D0%92%D1%82%D0%BE%D1%80%D0%B0%D1%8F_%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%8F_%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0",
    "https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D0%B5%D0%B2",
    "https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B0%D1%8F_%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%8F_%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0"
]

for url in urls:
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    if search_text in soup.get_text():
        print(f"Текст найден на сайте: {url}")