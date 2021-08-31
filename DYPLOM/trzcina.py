import bs4
import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.trzcinabistro.pl/restauracja/trzcina-bistro"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("li", {"class":"m-list__item"})
container = containers[0]

filename = "trzcina.csv"

with io.open(filename, "w", encoding="utf-8") as f:
    headers = "Nazwa | Opis |Cena\n"
    f.write(headers)

    for container in containers:
        nazwy = container.findAll("h4", {"class":"m-item__title restaurant-menu__dish-name"})
        nazwa1 = nazwy[0].text.replace("\n                  \n\n\n","")
        nazwa = nazwa1.replace("\n","")
        ceny = container.findAll("div", {"class":"m-item__col m-item__col--secondary actions"})
        cena_0 = ceny[0].button.text
        cena1 = cena_0.replace("zł","")
        cena2 = cena1.replace("\n","")
        cena3 = cena2.replace("                \xa0                ",",")
        cena4 = cena3.replace(" \n                \xa0\n                \n\n\n","")
        cena = cena4.replace(" ,","")
        opisy = container.findAll("div", {"class":"m-item__description"})
        opis = opisy[0].span.text

        print("nazwa: " + nazwa)
        print("opis: " + opis)
        print("cena: " + cena)

        f.write(nazwa + "|" + opis + "|" + cena + "\n")
