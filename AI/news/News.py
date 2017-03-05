import requests
import bs4
import urllib3
from bs4 import BeautifulSoup
import urllib.request
import re
import json
import os

url = 'http://api.nytimes.com/svc/topstories/v2/home.json?api-key=9f9d06f90e364ec9bdcf8119f14573dd'

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
data = json.loads(str(soup))
base = 'From the %s subsection of the %s section : %s : %s' %(data['results'][0]['subsection'], data['results'][0]['section'], data['results'][0]['title'], data['results'][0]['abstract'])
os.system("espeak --stdout '%s' -a 300 -s 130  | aplay" % base)

link = 'In other news...'
os.system("espeak --stdout '%s' -a 300 -s 130  | aplay" % link)

length = len(data['results'])

for i in range(1, length):
    rest = '%s : %s' %(data['results'][i]['title'], data['results'][i]['abstract'])
    os.system("espeak --stdout '%s' -a 300 -s 130 | aplay" % rest)
    i+=1




