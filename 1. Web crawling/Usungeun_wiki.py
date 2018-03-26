from bs4 import BeautifulSoup
import urllib.request as req

url = "https://ko.wikipedia.org/wiki/%EC%9C%A0%EC%84%B1%EC%9D%80"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

music_list = soup.select("#mw-content-text > div > ul > li")

for a in music_list :
    name = a.string
    if name == None : continue
    if name == "유튜브 채널" :
        print("+ Youtube Channel "+name)
        continue
    print("+", name)
