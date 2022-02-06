# UAS SUSULAN
Nama    : Putry Delsa Hasanah

NIM     : 312110019

Kelas   : TI.21.A.1

Mata Kuliah : Bahasa Pemrograman 

## Program Sederhana Melakukan Scraping Data Web (BeautifulSoap4.)

### Scraping Data Perkembangan Virus Covid-19

- Berikut merupakan scriptnya :

> import requests
from bs4 import BeautifulSoup
print("Web Scraping - Covid19 wordmeters.info")
print()
Negara = input("Masukan Nama Negara : ")
print()
page = requests.get("https://www.worldometers.info/coronavirus/country/{}/".format(Negara))
soup = BeautifulSoup(page.content, "html.parser")
data = soup.find("div", "content-inner").text.strip()
print(data)

![gambar](ScreenShot/satu.png)
 
- Berikut adalah outputnya
![gambar](ScreenShot/dua.png)

#### Sekian Terima Kasih
