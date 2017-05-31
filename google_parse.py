from lxml.html import fromstring
from urllib.parse import parse_qs,urlparse

import requests
html=requests.get('https://www.google.com/search?q=python3')


tree=fromstring(html.content)
links=[]

results=tree.cssselect('h3.r a')
for result in results:
    link =result.get('href')
    qs=urlparse(link).query
    links.extend(parse_qs(qs).get('q',[]))



print(links)
