#------------------------------MAXIPIZZA--------------------#
import bs4
import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

mp_url = 'https://www.maxipizza.pl/kielce,menu,internet'
kebab_url = "https://glovoapp.com/pl/waw/store/adel-kebab-waw/"
sushi_url = "https://sushi-master.pl/kielce/menu/sets/"
trzcina_url = "https://www.trzcinabistro.pl/restauracja/trzcina-bistro"
mc_url = "https://glovoapp.com/pl/waw/store/mcdonald-s-waw/collection/142924275/"

# Połączenie oraz pobranie strony 
uClient_mp = uReq(mp_url)
page_html_mp = uClient_mp.read()
uClient_mp.close()

#parsowanie HTML
page_soup_mp = soup(page_html_mp, "html.parser")

#określenie frejma produktu
containers_mp = page_soup_mp.findAll("div", {"class":"pizza-placeholder"})
container_mp = containers_mp[0]
tekst_mp = container_mp.h4.get_text()


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
my_str = multiple_replace(tekst_mp, replace_values)

filename_mp = "Menu.csv"
with io.open(filename_mp, "w", encoding="utf-8") as f_mp:
    headers_mp = "Nazwa | Skladniki | Cena\n"
    f_mp.write(headers_mp)

    for container_mp in containers_mp:
        nazwy_mp = container_mp.findAll("h4", {"class":"towar-nazwa"})
        nazwas_mp = nazwy_mp[0].text
        nazwa_mp = multiple_replace(nazwas_mp, replace_values)
        opis_piz = container_mp.findAll("span",{"class":"towar-description"})
        opis_pizz = opis_piz[0].text
        ceny_mp = container_mp.findAll("div", {"class":"hidden-xs col-sm-2 col-md-2 col-lg-1"})
        cena_mp_0 = ceny_mp[0]
        cena_mp = cena_mp_0.div.div.div.text.replace("zł","")

        print("nazwa: " + nazwa_mp)
        print("opis_pizz: " + opis_pizz)
        print("cena: " + cena_mp)

        f_mp.write(nazwa_mp + "|" + opis_pizz + "|" + cena_mp + "\n")

#-------------------------GLOVO_KEBAB-----------------------#

uClient_kebab = uReq(kebab_url)
page_html_kebab = uClient_kebab.read()
uClient_kebab.close()

page_soup_kebab = soup(page_html_kebab, "html.parser")
containers_kebab = page_soup_kebab.findAll("div", {"class":"card-content"})
container_kebab = containers_kebab[0]

filename_kebab = "Glovo_kebab.csv"

with io.open(filename_kebab, "w", encoding="utf-8") as f_kebab:
    headers_kebab = "Nazwa | Cena\n"
    f_kebab.write(headers_kebab)

    for container_kebab in containers_kebab:
        nazwy_kebab = container_kebab.findAll("h4", {"class":"title"})
        nazwa_kebab = nazwy_kebab[0].text
        ceny_kebab = container_kebab.findAll("span", {"class":"price__effective"})
        cena_kebab_0 = ceny_kebab[0]
        cena1_kebab = cena_kebab_0.text.replace("zł","")
        cena2_kebab = cena1_kebab.replace("XOF","")
        cena_kebab = cena2_kebab.replace(".",",")

        print("nazwa: " + nazwa_kebab)
        print("cena: " + cena_kebab)

        f_kebab.write(nazwa_kebab + "|" + cena_kebab + "\n")

#-------------------------SUSHIMASTER-----------------------#

uClient_sushi = uReq(sushi_url)
page_html_sushi = uClient_sushi.read()
uClient_sushi.close()

page_soup_sushi = soup(page_html_sushi, "html.parser")
containers_sushi = page_soup_sushi.findAll("div", {"class":"item-long item__el item__el-get buySushi"})
container_sushi = containers_sushi[0]

filename_sushi = "Sushi.csv"

with io.open(filename_sushi, "w", encoding="utf-8") as f_sushi:
    headers_sushi = "Nazwa | Składniki | Cena | Link\n"
    f_sushi.write(headers_sushi)

    for container_sushi in containers_sushi:
        nazwy_sushi = container_sushi.findAll("span", {"class":"item__name"})
        nazwa_sushi = nazwy_sushi[0].text
        opisy_sushi = container_sushi.findAll("div", {"class":"item-long__text"})
        opis1_sushi = opisy_sushi[0].text
        opis_sushi = opis1_sushi.replace("...","")
        ceny_sushi = container_sushi.findAll("div", {"class":"item-long__cost"})
        cena_0_sushi = ceny_sushi[0]
        cena1_sushi = cena_0_sushi.text.replace("zł","")
        cena_sushi = cena1_sushi.replace(".",",")
        links_sushi = container_sushi.findAll("a",{"class":"item-long__wraper"})
        link_sushi = links_sushi[0]
        linkp_sushi = "https://sushi-master.pl" + link_sushi['href']
        uClient1_sushi = uReq(linkp_sushi)
        page_html1_sushi = uClient1_sushi.read()
        uClient1_sushi.close()
        page_soup1_sushi = soup(page_html1_sushi, "html.parser")
        containers1_sushi = page_soup1_sushi.findAll("div", {"class":"case-wraper"})
        container1_sushi = containers1_sushi[0]

        for container1_sushi in containers1_sushi:
            imgs_sushi = container1_sushi.findAll("a",{"class":"case-img__item"})
            img1_sushi = imgs_sushi[0]
            img_sushi = img1_sushi['href']
            img2_sushi = "https://sushi-master.pl" + img_sushi
            


        print("nazwa: " + nazwa_sushi)
        print("opis: " + opis_sushi)
        print("cena: " + cena_sushi)
        print("link: " + img_sushi)


        f_sushi.write(nazwa_sushi + "|" + opis_sushi + "|" + cena_sushi + "|" + img_sushi + "\n")

#---------------------------TRZCINA--------------------#

uClient_trzcina = uReq(trzcina_url)
page_html_trzcina = uClient_trzcina.read()
uClient_trzcina.close()

page_soup_trzcina = soup(page_html_trzcina, "html.parser")
containers_trzcina = page_soup_trzcina.findAll("li", {"class":"m-list__item"})
container_trzcina = containers_trzcina[0]

filename_trzcina = "trzcina.csv"

with io.open(filename_trzcina, "w", encoding="utf-8") as f_trzcina:
    headers_trzcina = "Nazwa | Opis |Cena\n"
    f_trzcina.write(headers_trzcina)

    for container_trzcina in containers_trzcina:
        nazwy_trzcina = container_trzcina.findAll("h4", {"class":"m-item__title restaurant-menu__dish-name"})
        nazwa1_trzcina = nazwy_trzcina[0].text.replace("\n                  \n\n\n","")
        nazwa_trzcina = nazwa1_trzcina.replace("\n","")
        ceny_trzcina = container_trzcina.findAll("div", {"class":"m-item__col m-item__col--secondary actions"})
        cena_0_trzcina = ceny_trzcina[0].button.text
        cena1_trzcina = cena_0_trzcina.replace("zł","")
        cena2_trzcina = cena1_trzcina.replace("\n","")
        cena3_trzcina = cena2_trzcina.replace("                \xa0                ",",")
        cena4_trzcina = cena3_trzcina.replace(" \n                \xa0\n                \n\n\n","")
        cena_trzcina = cena4_trzcina.replace(" ,","")
        opisy_trzcina = container_trzcina.findAll("div", {"class":"m-item__description"})
        opis_trzcina = opisy_trzcina[0].span.text

        print("nazwa: " + nazwa_trzcina)
        print("opis: " + opis_trzcina)
        print("cena: " + cena_trzcina)

        f_trzcina.write(nazwa_trzcina + "|" + opis_trzcina + "|" + cena_trzcina + "\n")
        

#--------------------------McDonalds-------------------#

uClient_mc = uReq(mc_url)
page_html_mc = uClient_mc.read()
uClient_mc.close()

page_soup_mc = soup(page_html_mc, "html.parser")
containers_mc = page_soup_mc.findAll("div", {"class":"card-content"})
container_mc = containers_mc[0]

filename_mc = "Glovo_mc.csv"

with io.open(filename_mc, "w", encoding="utf-8") as f_mc:
    headers_mc = "Nazwa | Cena\n"
    f_mc.write(headers_mc)

    for container_mc in containers_mc:
        nazwy_mc = container_mc.findAll("h4", {"class":"title"})
        nazwa_mc = nazwy_mc[0].text.replace("®","")
        ceny_mc = container_mc.findAll("span", {"class":"price__effective"})
        cena_0_mc = ceny_mc[0]
        cena1_mc = cena_0_mc.text.replace("zł","")
        cena2_mc = cena1_mc.replace("MAD","")
        cena_mc = cena2_mc.replace(".",",")

        print("nazwa: " + nazwa_mc)
        print("cena: " + cena_mc)

        f_mc.write(nazwa_mc + "|" + cena_mc + "\n")






