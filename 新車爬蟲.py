#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import time
res=requests.get("https://autos.yahoo.com.tw/car-search?price_range=150-200")
soup=BeautifulSoup(res.text)
car=soup.find_all("div",class_="model-wrapper")
price=["0.01-60","60-100","100-150","150-200","200-250","250-400","400"]
for k in range(len(price)):
    for j in range(1,10):
        res=requests.get("https://autos.yahoo.com.tw/car-search?price_range="+price[k]+"&p="+str(j))
        soup=BeautifulSoup(res.text)
        car=soup.find_all("div",class_="model-wrapper")
        if car==[]:
            break
        else:
            for i in range(len(car)):
                print(car[i].find_all("span")[0].text.replace(" ","").replace("\n",""))
                print(car[i].find_all("span")[1].text.replace(" ","").replace("\n",""))
                print(car[i].find_all("li",class_="model-sub")[0].ul.find_all("li")[-1].text)
                print(car[i].ul.a["href"])
                print("------------------------------------")
            print(f"{k}第{j}頁")
            time.sleep(5)

