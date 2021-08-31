import bs4
import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://sushi-master.pl/kielce/menu/sets/"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-long item__el item__el-get buySushi"})
container = containers[0]

filename = "Sushi.csv"

with io.open(filename, "w", encoding="utf-8") as f:
    headers = "Nazwa | Składniki | Cena | Link\n"
    f.write(headers)

    for container in containers:
        nazwy = container.findAll("span", {"class":"item__name"})
        nazwa = nazwy[0].text
        opisy = container.findAll("div", {"class":"item-long__text"})
        opis1 = opisy[0].text
        opis = opis1.replace("...","")
        ceny = container.findAll("div", {"class":"item-long__cost"})
        cena_0 = ceny[0]
        cena1 = cena_0.text.replace("zł","")
        cena = cena1.replace(".",",")
        links = container.findAll("a",{"class":"item-long__wraper"})
        link = links[0]
        linkp = "https://sushi-master.pl" + link['href']
        uClient1 = uReq(linkp)
        page_html1 = uClient1.read()
        uClient1.close()
        page_soup1 = soup(page_html1, "html.parser")
        containers1 = page_soup1.findAll("div", {"class":"case-wraper"})
        container1 = containers[0]

        for container1 in containers1:
            imgs = container1.findAll("a",{"class":"case-img__item"})
            img1 = imgs[0]
            img = img1['href']
            img2 = "https://sushi-master.pl" + img
            


        print("nazwa: " + nazwa)
        print("opis: " + opis)
        print("cena: " + cena)
        print("link: " + img )



        

        f.write(nazwa + "|" + opis + "|" + cena + "|" + img + "\n")









