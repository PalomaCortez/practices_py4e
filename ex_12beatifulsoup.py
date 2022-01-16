# Practice with Python - HTTP with BeautifulSoup

#importing text from http
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the link: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retreive all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
