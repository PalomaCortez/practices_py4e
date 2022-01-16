# Practice with Python
# handling JSON data

import urllib.request, urllib.parse, urllib.error
import json
import ssl


url = input("Enter location: ")

try:
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print('Retrieving', url)
    # if there is no need of key to access the data
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    content = json.loads(data)

    # 1st we limit the seach on 'comments'
    # counts gives positions of the tag counts, we need to get the text from it
    nums = []
    for item in content['comments']:
        nums.append(item['count'])  # already an int

    print('count', len(nums))
    print(sum(nums))
except:
    print("URL improperly formatted or non-existent")
    exit()
