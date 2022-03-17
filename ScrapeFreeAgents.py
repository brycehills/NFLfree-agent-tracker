from json.encoder import JSONEncoder
from bs4 import BeautifulSoup
import numpy as np
from urllib.request import urlopen as request
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
from operator import itemgetter
import json


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

r = requests.get(url)
df_list = pd.read_html(r.text) # parse html table to list
print(df_list)
#df_list.append(names)

#iterate over list of dfs and convert to json objects
df_list_json= []
length = len(df_list)
for i in range(length):
    df_list_json.append(df_list[i].to_json())

jsonStr = json.dumps(df_list_json)
json_names_str = json.dumps(names)
with open("output.txt", 'w') as outfile:
    outfile.write(json_names_str)
    outfile.write(jsonStr)
