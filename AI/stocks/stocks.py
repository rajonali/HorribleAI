import urllib3
import csv
import re
import requests
import time
import os

'''
Obtain stocks to parse from text file and create readable string to input into espeak.
'''


def getStocks():
    symbolsfile = open('stocks.list')
    symbolslist = symbolsfile.read()
    newsymbolslist = symbolslist.split(',')
    return newsymbolslist

def priceOutput(stock):
    url="http://query.yahooapis.com/v1/public/yql?q=select%20%2a%20from%20yahoo.finance.quotes%20where%20symbol%20in%20%28%22"+stock+"%22%29%0A%09%09&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"
    data = requests.get(url).json()
    output = 'The price of %s is %s'%(data['query']['results']['quote']['Name'],data['query']['results']['quote']['LastTradePriceOnly'])
    return output

def __main__()
    for i in getStocks():
        os.system("espeak '%s' -s 100" % i)
    '''
    mp3url = 'http://tts-api.com/tts.mp3?q='+output.replace(' ', '_').replace('&', ' and ')+''
    with open('%s.mp3'%data['query']['results']['quote']['Name'].replace(' ',' '), 'wb') as handle:
        response = requests.get(mp3url, stream=True)
        if not response.ok:
            print('Something went wrong :(')
        for block in response.iter_content(1024):
            handle.write(block)
    '''
