from dataclasses import replace
from bs4 import BeautifulSoup
import requests
import sys

# Contoh kita ambil informasi coin crypto baru di coinmarketcap.com

r = requests.get('https://coinmarketcap.com/new/')
base_url = 'https://coinmarketcap.com'
url_baru = []

soup = BeautifulSoup(r.text)
# print(soup.title.string)

for link in soup.find_all('a'):
    url = link.get('href')
    if url and '/currencies/' in url and '/climate/united-states/us' not in url:
        url_baru.append(url)
# print(state_links)

f = open("test.txt", "a")

for i in url_baru:
    if i.find("bitcoin") != -1:
        pass
    elif i.find("axie-infinity") != -1:
        pass
    elif i.find("axie-infinity") != -1:
        pass
    elif i.find("smooth-love-potion") != -1:
        pass
    elif i.find("ether") != -1:
        pass
    elif i.find("soup") != -1:
        pass
    else:
        print(i.replace("/currencies/",
              "https://coinmarketcap.com/currencies/"), file=f)
f.close()
