from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html.read(),"lxml")

nameList = bsobj.findAll("span",{"class":"green"})
print(nameList[0].get_text())
# for name in nameList:
#     print(name.get_text())

nameList2 = bsobj.findAll(text = "the prince")
# print(nameList2)
print(len(nameList2))
# for name in nameList2:
#     print(name)

# allText = bsobj.findAll(id = "text")
# print(allText[0].get_text())

allText = bsobj.findAll("", {"id":"text"})
print(allText[0].get_text())  #为什么这里是零，因为全文只有一对text标签
# for text in allText:
#     print(text.get_text())