from dataclasses import replace
from bs4 import BeautifulSoup
import requests
import sys


def prosesAmbilData(inputUrl):
    r = requests.get(inputUrl)

    base_url = inputUrl
    url_baru = []

    soup = BeautifulSoup(r.text)

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


def main():
    inputUrl = input("Masukkan URL : ")
    prosesAmbilData(inputUrl)


if __name__ == "__main__":
    main()
