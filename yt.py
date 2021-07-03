import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re
import time

def ytb(cha:str):
    temp = cha
    cha = cha.replace("https://www.youtube.com/channel/","")
    url = "https://playboard.co/en/channel/" + cha

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

        
    result1 = soup.find_all(class_ = "stats stats--clickable")

    sub = re.search(r'Subscribers</li><li class="num" data-v-731a73a9="">\n.*', str(result1)).group().replace("Subscribers</li><li class=\"num\" data-v-731a73a9=\"\">\n","").strip()
    view = re.search(r'Views</li><li class="num" data-v-731a73a9="">\n.*', str(result1)).group().replace("Views</li><li class=\"num\" data-v-731a73a9=\"\">\n","").strip()
    sc = re.search(r'Super Chat</li><li class="num" data-v-731a73a9="">\n.*', str(result1)).group().replace("Super Chat</li><li class=\"num\" data-v-731a73a9=\"\">\n","").strip()

    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
        
    scurl = "https://www.google.com/search?q=USD+NT%E8%BD%89%E6%8F%9B&oq=usd&aqs=chrome.0.69i59j69i57j69i60l3.11756j0j15&sourceid=chrome&ie=UTF-8"
    res = requests.get(scurl, headers = headers)
    so = BeautifulSoup(res.text, "html.parser")
    res = so.find(class_ = "dDoNo ikb4Bb gsrt gzfeS")
        
    namesoup = soup.find(class_ = "name")
    name = re.search(r'data-v-731a73a9="">.*<svg', str(namesoup)).group().replace("data-v-731a73a9=\"\">","").replace("<svg","")
        
    print(name + "\nSubscribers : " + sub + "\nViews : " + view + "\nSuper Chat : " + sc)
    
        

def vtbsc(tag):
    url = "https://playboard.co/en/youtube-ranking/most-superchatted-v-tuber-channels-in-worldwide-"
    if tag == "day":
        url = url + "daily"
    elif tag == "week":
        url = url + "weekly"
    elif tag == "month":
        url = url + "monthly"     
        
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
                
    result = list(soup.find_all("h3"))
    name = []
    x = 1
    for i in result:
        if x > 5:
            if x == 16:
                break
            name.append(str(i).replace("<h3 data-v-35d0e4bd=\"\">", "").replace("</h3>",""))
            x += 1
        else:
            x += 1

    result = soup.find_all(class_ = "fluc-label fluc-label--mono-font fluc-label--en fluc-label--symbol-math up")
    sc = []
    x = 1
    for i in result:
        if x != 11:
            sc.append(str(i).replace("<span class=\"fluc-label fluc-label--mono-font fluc-label--en fluc-label--symbol-math up\" data-v-35d0e4bd=\"\" data-v-937592aa=\"\">", "").replace("</span>",""))
            x += 1
        else:
            break

    get_date = list(soup.find_all(class_ = "item item--selected"))
    date = str(get_date[-1]).replace("<li class=\"item item--selected\" data-v-b29c4886=\"\"><span class=\"item__label\" data-v-b29c4886=\"\">", "").replace("</span></li>","").strip()

    print(date)
    for i in range(10):
        print("No.%-2s" % (i+1) + name[i] + "\n\t\t\t\t" + sc[i])

x = input("input command : ")
if x == "ytb":
    urls = input()
    ytb(urls)
elif x == "vtbsc":
    tags = input()
    vtbsc(tags)


