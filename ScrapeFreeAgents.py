from bs4 import BeautifulSoup
import numpy as np
from urllib.request import urlopen as request
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

url = "https://www.spotrac.com/nfl/free-agents/"

res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')

#decompose span elements
spans = soup.findAll('span')
for match in spans:
    match.decompose()

#find names
names=[]
for item in soup.find_all("td", {"class" : "player"})[:100]:
        names.append(item.text)

print(names)
#insert names into pd df at row 1

#r = requests.get(url)
#df_list = pd.read_html(r.text) # parse html table to list

#attempt ot grab nested player name data
#print(df_list)

#print(df_list)
#df = df_list[0]
#print(df)


