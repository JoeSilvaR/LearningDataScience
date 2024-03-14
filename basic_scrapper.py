# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:16:02 2023

@author: josep
"""
import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/Main_Page").text

#Creating Beautiful Soup Object
soup = BeautifulSoup(page, 'html.parser')

#Pull  all Instances of <a> tag
artists = soup.find_all('a')

#Clears data of all tags
for artist in artists:
    names = artist.contents[0]
    fulllink = artist.get('href')
    print(names)
    print(fulllink)
