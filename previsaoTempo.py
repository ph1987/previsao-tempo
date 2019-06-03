# scraping for weather

import requests
from bs4 import BeautifulSoup as bs

def roundTemp(temp):
    if (temp != "-"):
        tempDot = temp.replace(",",".")
        t = tempDot.split(" ")
        tempFloat = float(t[0])
        tempInt = int(round(tempFloat, 0))
        formattedTemp = str(tempInt) + t[1]
        return formattedTemp
    else:
        return temp

def getregion(city):
    if (city == 'SAO PAULO' or city == 'RIO DE JANEIRO' or city == 'VITORIA' or city == 'BELO HORIZONTE'):
        return "SUDESTE"
    elif (city == 'PORTO ALEGRE' or city == 'FLORIANOPOLIS' or city == 'CURITIBA'):
        return "SUL"
    elif (city == 'BRASILIA' or city == 'GOIANIA' or city == 'CAMPO GRANDE' or city == 'CUIABA'):
        return "CENTRO-OESTE"
    elif (city == 'MANAUS' or city == 'BOA VISTA' or city == 'PALMAS' or city == 'RIO BRANCO' or city == 'PORTO VELHO' or city == 'MACAPA' or city == 'BELEM'):
        return "NORTE"
    else:
        return "NORDESTE"

class City:
    def __init__(self, city, tempmin, tempmax, umidrel, rain):
        self.city = city
        self.tempmin = roundTemp(tempmin.strip())
        self.tempmax = roundTemp(tempmax.strip())
        self.umidrel = umidrel.strip()
        self.rain = rain.strip()
        self.region = getregion(self.city)

url = 'http://www.inmet.gov.br/sim/cond_reg/tempoCapitais.php'

page = requests.get(url)
soup = bs(page.text, 'html.parser')
trs = soup.findAll('tr')

tds = []
i = 0
for tr in trs:
    if (i>2 and i < 30):
        tds.append(tr.get_text().split('\n'))
    i += 1

cityList = []
for td in tds:
    cityList.append(City(td[1],td[2],td[3],td[4],td[5]))
'''  
for c in cityList:
    print(c.city + " | ⬇️ " + c.tempmin + " | ⬆️ " + c.tempmax + " | " + c.umidrel + " | " + c.rain + " | " + c.region)
'''
SEList = (x for x in cityList if x.region == "SUDESTE")
for item in SEList:
    print(item.city + " ️️️️⬆️ " + item.tempmax + " ️⬇️ " + item.tempmin)

print("\n")

SList = (x for x in cityList if x.region == "SUL")
for item in SList:
    print(item.city + " ⬆️ " + item.tempmax + " ⬇️ " + item.tempmin)

print("\n")

COList = (x for x in cityList if x.region == "CENTRO-OESTE")
for item in COList:
    print(item.city + " ⬆️ " + item.tempmax + " ⬇️ " + item.tempmin)

print("\n")

NEList = (x for x in cityList if x.region == "NORDESTE")
for item in NEList:
    print(item.city + " ⬆️ " + item.tempmax + " ⬇️ " + item.tempmin)

print("\n")

NList = (x for x in cityList if x.region == "NORTE")
for item in NList:
    print(item.city + " ⬆️ " + item.tempmax + " ⬇️ " + item.tempmin)