import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import re
import time


'''
Type a number after the command to find the manga in nhentxx
plus "show" after number to display first pic
For example: 
!nfind 362638 show
'''
def nfind(num, show = None):
    url = "https://nhentai.net/g/"

    url = url + str(num)
    response = requests.get(url)

    print("try to get website...")
    if response.status_code == 404:
        print("can't find the page")
        return
    elif response.status_code == 200:
        print("get page successful...") 
        print(url)

    soup = BeautifulSoup(response.text, "html.parser")
    pic_url = soup.find(id = "cover").find("a").find("img")["data-src"]
    if show == "show":
        print(pic_url)


def ntag(tag, show = None):
    url = "https://nhentai.net/tag/"
        
    url = url + str(tag)
    print(url)
    response = requests.get(url)

    print("try to get website...")
    if response.status_code == 404:
        print("can't find the tag")
        return
    elif response.status_code == 200:
        print("get page successful ! ") 

    soup = BeautifulSoup(response.text, "html.parser")
    response = soup.find_all(class_ = "gallery")

    pic_url = re.findall(r'data-src=".*?[jpg]*[png]*"' , str(response))

    num = re.findall(r'href=".*?/"' , str(response))

    list1 = []

    k = 1
    for i in num:
        urls = re.search(r'/g/[0-9]{6}/', i).group()
        list1.append("https://nhentai.net" + urls)
        if k == 3:
            break
        k += 1
        
    if show == "show":
        k = 1
        for i in pic_url:
            picurl = re.search(r'https://.*[jpg]*[png]*[^"]', i).group()
            list1.append(picurl)
            if k == 3:
                break
            k += 1

    k = 1
    for i in range(5):
        print(list1[i])
        if show == "show":
            print(list1[i + 3])
        time.sleep(1)
        if k == 3:
            return
        k += 1

i = input("please choose a funtion(nfind / ntag):")
if i == "nfind":
    k = input("input number")
    nfind(k)
elif i == "ntag":
    k = input("input number")
    nfind(k)