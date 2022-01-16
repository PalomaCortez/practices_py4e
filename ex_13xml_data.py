# Practice with Python
# handling XML data

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


url = input("Enter location: ")

try:
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print('Retrieving', url)
    # There is no need of key to access he data
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    # counts gives positions of the tag counts, we need to get the text from it
    nums = []
    for count in counts:
        nums.append(int(count.text))  # text must be converted to int
    print('count', len(nums))
    print(sum(nums))
except:
    print("URL improperly formatted or non-existent")
    exit()
