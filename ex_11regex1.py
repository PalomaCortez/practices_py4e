# Practice with Python Regular Expressions
# counting word frequency in a file
import re


rgxp = input('Enter a regular expression: ')
hand =  open('mbox.txt')

cnt = 0
for line in hand:
    line = line.rstrip()
    if re.findall(rgxp, line):
        cnt += 1

print(cnt)
