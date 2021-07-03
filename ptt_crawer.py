from bs4 import BeautifulSoup
from pprint import pprint
import requests

r = requests.get('https://www.ptt.cc/bbs/NTU/index.html')

soup = BeautifulSoup(r.text, "html.parser")
results = soup.select("#main-container > div.r-list-container.action-bar-margin.bbs-screen > div:nth-child(3) > div.title > a")
result_url = results[0].attrs['href']
print(result_url)

request_r = requests.get("https://www.ptt.cc" + result_url)
result_soup = BeautifulSoup(request_r.text, "html.parser")

a = result_soup.find_all(class_='article-metaline')
for i in a:
    print(i.find(class_ = "article-meta-tag").text,end = " ")
    print(i.find(class_ = "article-meta-value").text)

print(a[-1].next_sibling)

r1 = requests.get("https://www.imdb.com/search/title/?groups=top_100")
soup1 = BeautifulSoup(r1.text, "html.parser")

result1 = soup1.find_all(class_ = "lister-item-header")
movie_list = []
for line in result1:
    movie_list.append(line.find("a").text)
pprint(movie_list)

result2 = soup1.find_all(class_ = "genre")
gen_list = []
for line in result2:
    gen_list.append(line.text.strip().split(", "))
pprint(gen_list)


pprint(list(zip(movie_list, gen_list)))

