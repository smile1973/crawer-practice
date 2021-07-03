from bs4 import BeautifulSoup
from pprint import pprint
import requests

r = requests.get('https://www.ptt.cc/bbs/NTU/index.html')

soup = BeautifulSoup(r.text, "html.parser")
results = soup.select("#main-container > div.r-list-container.action-bar-margin.bbs-screen > div:nth-child(2) > div.title > a")
result_url = results[0].attrs['href']
print(result_url)

request_r = requests.get("https://www.ptt.cc" + result_url)
result_soup = BeautifulSoup(request_r.text, "html.parser")

a = result_soup.find_all(class_='article-metaline')
for i in a:
    print(i.find(class_ = "article-meta-tag").text,end = " ")
    print(i.find(class_ = "article-meta-value").text)

print(a[-1].next_sibling)



