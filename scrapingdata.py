import requests
from bs4 import BeautifulSoup

print("Web Scraping - Covid19 wordmeters.info")
print()
Negara = input("Masukan Nama Negara : ")
print()
page = requests.get("https://www.worldometers.info/coronavirus/country/{}/".format(Negara))

soup = BeautifulSoup(page.content, "html.parser")
data = soup.find("div", "content-inner").text.strip()

print(data)
 