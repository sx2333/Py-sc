# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsobj = BeautifulSoup(html.read())
# print(bsobj.h1）
 
# try:
#     print("i'm try")
# except:
#     print("i'm except")
# else:
#     print("I am else")

# try:
#     print(1/0)
# except:
#     print("i am except")
# else:
#     print()

# while 1:
#     try:
#         x = input("the first number")
#         y = input("the second number")
#         r =  x/y
#         print(y)
#     except Exception as e:  #不管是什么异常，这里都会捕获，然后传给e
#         print(e)
#         print("try again")
#     else:
#         break
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle(" http://www.pythonscraping.com/pages/warandpeace.html ")
if title == None:
    print("tltle could not found")
else:
    print(title)

