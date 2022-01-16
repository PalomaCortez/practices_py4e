# Practice with Python - HTTP

'''
 py4e book 12.2:Change your socket program so that it counts the number of
 characters it has received and stops displaying any text after it has shown
 3000 characters. The program should retrieve the entire document and count the
 total number of characters and display the count of the number of characters
 at the end of the document.

12.3: Use urllib to replicate the previous exercise of (1) retrieving the
document from a URL, (2) displaying up to 3000 characters, and (3) counting
the overall number of characters in the document. Don’t worry about the headers
for this exercise, simply show the first 3000 characters of the document
contents.
'''

#importing text from http
import urllib.request


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')


address = input("Enter the link: ")

try:
    html = urllib.request.urlopen(address).read()

    for line in html:
        text = html.decode()
        if len(text) < 1:
            break

    print(text[:3000])
    print(len(text))

#
except:
    print("URL improperly formatted or non-existent")
    exit()
