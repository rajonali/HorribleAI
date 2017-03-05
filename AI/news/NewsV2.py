import requests
import bs4
import urllib3
from bs4 import BeautifulSoup
import urllib.request
import re
import json
import os


'''
Obtain news to parse from NY Times API and create readable string to input into espeak.
'''


url = 'http://api.nytimes.com/svc/topstories/v2/home.json?api-key=9f9d06f90e364ec9bdcf8119f14573dd'

def getJson():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    data = json.loads(str(soup))
    return data

def finalData(json):
    base = 'From the %s subsection of the %s section : %s : %s' %(json['results'][0]['subsection'], json['results'][0]['section'], json['results'][0]['title'], json['results'][0]['abstract'])
    return base

def link():
    link = 'In other news...'
    #print(link)
    return link


def restNews(json):
    newsList = []
    length = len(json['results'])
    for i in range(1, length):
        rest = '%s : %s' %(json['results'][i]['title'], json['results'][i]['abstract'])
        newsList.append(rest)
    return newsList

def __main__():
    json = getJson()
    text = finalData(json)+ " " +link()
    for i in restNews(json):
        text+=i
    print(text)
    os.system('espeak "%s"'% text)



__main__()

