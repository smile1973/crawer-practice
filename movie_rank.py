from bs4 import BeautifulSoup
from pprint import pprint
import requests

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