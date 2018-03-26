from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.goal.com/kr/%ED%94%84%EB%A6%AC%EB%AF%B8%EC%96%B4-%EB%A6%AC%EA%B7%B8/%EC%88%9C%EC%9C%84/2kwbbcootiqqgmrzs6o5inle5"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

epl_list = soup.select("body > div.page-container > div.page-container-bg > div.mr-gutters.main-container.clearfix > div > div > div.table > div.table__body > div > div:nth-of-type(3) > a")
score = soup.select("body > div.page-container > div.page-container-bg > div.mr-gutters.main-container.clearfix > div > div > div.table > div.table__body > div > div:nth-of-type(9)")
name1 = []
name2 = []

for a in epl_list :
    name1.append(a.string)

for a in score:
    name2.append(a.string)

for i in range(0,20) :
    print("rank :",i+1," team :",name1[i],", score :",name2[i])
