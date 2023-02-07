from bs4 import BeautifulSoup
import requests

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


for i in url_baru:
    print(i)
