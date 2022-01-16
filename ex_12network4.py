# Practice with Python - HTTP with BeautifulSoup

'''
py4e book 12.4: Change the urllinks.py program to extract and count paragraph
(p) tags from the retrieved HTML document and display the count of the
paragraphs as the output of your program. Do not display the paragraph text,
only count them. Test your program on several small web pages as well as some
larger web pages.
'''

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

nums = []
tags = soup('span')

for tag in tags:
    found = re.findall('[0-9]+', str(tag))
    if found:
        nums.append(int(found[0]))

print(sum(nums))













# nums = []

# for line in soup:
    # line = line.rstrip('<')
    # print(line)
#     found = re.findall('([0-9]+)</span></td></tr>$', tag)
#     if found:
#         nums.append(int(found[0]))  # because found is a list
#
# print(nums)
# print(sum(nums)//len(nums))
