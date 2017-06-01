from urllib.request import urlopen

from bs4 import BeautifulSoup


html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")


bsObj=BeautifulSoup(html,"lxml")


nameList=bsObj.findAll("span",{'class':'green'})

#find the number of times prince only
nameList=bsObj.findAll(text="the prince")

print(len(nameList))
#for name in nameList:
#    print(name.get_text())
