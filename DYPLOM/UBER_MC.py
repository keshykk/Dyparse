import bs4
import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://glovoapp.com/pl/waw/store/mcdonald-s-waw/collection/142924275/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"card-content"})
container = containers[0]

filename = "Glovo_mc.csv"

with io.open(filename, "w", encoding="utf-8") as f:
    headers = "Nazwa | Cena\n"
    f.write(headers)

    for container in containers:
        nazwy = container.findAll("h4", {"class":"title"})
        nazwa = nazwy[0].text.replace("®","")
        ceny = container.findAll("span", {"class":"price__effective"})
        cena_0 = ceny[0]
        cena1 = cena_0.text.replace("zł","")
        cena2 = cena1.replace("MAD","")
        cena = cena2.replace(".",",")

        print("nazwa: " + nazwa)
        print("cena: " + cena)

        f.write(nazwa + "|" + cena + "\n")
