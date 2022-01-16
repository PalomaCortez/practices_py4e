# Practice with Python - HTTP assignment

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import re
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# nums = []
# tags = soup('span')
#
# for tag in tags:
#     found = re.findall('[0-9]+', str(tag))
#     if found:
#         nums.append(int(found[0]))
#
# print(sum(nums))



import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

def link_seeker(url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags_list = []
    tags = soup('a')
    for tag in tags:
        tags_list.append(tag.get('href', None))
    return tags_list

# To make a list of names from the links
def get_name(str):
    name = re.findall('([A-Z]+[a-z]+).html$', str)
    return name

urlink = input('Enter URL:')
name_str = []
position = int(input('Enter position:'))-1
repete = int(input('Enter count:'))+1

for i in range(repete):
    print('Retrieving: ', urlink)
    name_str.append(str(get_name(urlink)))
    tags_lst = link_seeker(urlink)
    urlink = tags_lst[position]


print(name_str[-1])
# print(tags_lst)



# str = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# name = re.findall('([A-Z]+[a-z]+).html$', str)
# print (name)




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
