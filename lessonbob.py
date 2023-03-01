# import urllib.request
import requests
from bs4 import BeautifulSoup
# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/get")
# print(response.read())
#
# response = requests.get("https://httpbin.org/get")
# print(response.text)
#
# response = requests.post("https://httpbin.org/post", data="Test data", headers={'h1': "Test title"})
# print(response.text)
#
# response = requests.get('https://coinmarketcap.com/')
#
# response_text = response.text
#
# response_parse = response_text.split('<span>')
# for elem in response_parse:
#     if elem.startswith("$"):
#         for elem_2 in elem.split("</span"):
#             if elem_2.startswith("$") and elem_2[1].isdigit():
#                 print(elem_2)

response = requests.get('https://coinmarketcap.com/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all('a', {"href": "/currencies/bitcoin/markets/"})
    res = soup_list[0].find("span")
    print(res.text)















