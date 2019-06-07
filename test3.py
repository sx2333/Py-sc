from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html,"lxml")

# for child in bsobj.find("table", {"id":"giftList"}).children:
#     print(child)

for sibling in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)