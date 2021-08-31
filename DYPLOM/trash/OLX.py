import bs4
import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.olx.pl/nieruchomosci/stancje-pokoje/kielce/'

# Połączenie oraz pobranie strony 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#parsowanie HTML
page_soup = soup(page_html, "html.parser")

#określenie frejma produktu
containers = page_soup.findAll("tr", {"class":"wrap"})
container = containers[0]

# Funkcja do znormalizowania HTML
def multiple_replace(target_str, replace_values):
    # pętla dla pobierania danych do zamiany
    for i, j in replace_values.items():
        # zamiana target_str
        target_str = target_str.replace(i, j)
    return target_str
# słownik wartości do zamiany
replace_values = {"\n": "", "\t": "", "\r": "", "1/2": ""}
# zmiana wartości początkowej


filename = "mieszkania.csv"
with io.open(filename, "w", encoding="utf-8") as f:
    headers = "Nazwa | Skladniki | Cena\n"
    f.write(headers)

    for container in containers:
        nazwy = container.findAll("h3", {"class":"lheight22 margintop5"})
        nazwa = nazwy[0].strong.text
        ceny = container.findAll("div", {"class":"space inlblk rel"})
        cena = ceny[0].p.strong.text
        links = container.findAll("a",{"class":"marginright5 link linkWithHash detailsLinkPromoted linkWithHashPromoted"})
        link = links[0]
        linkp = link['href']
        uClient1 = uReq(linkp)
        page_html1 = uClient1.read()
        uClient1.close()
        page_soup1 = soup(page_html1, "html.parser")
        containers1 = page_soup1.findAll("li", {"class":"offer-details__item"})
        container1 = containers[0]
        
        for container1 in containers1:
            imgs = container1.findAll("strong",{"class":"offer-details__value"})
            img1 = imgs[0]
            img = img1.text

        print("nazwa: " + nazwa)
        print("opis_pizz: " + img)
        print("cena: " + cena)

        f.write(nazwa + "|" + img + "|" + cena + "\n")

