# Practice with Python Regular Expressions

'''
py4e book 11.2: Write a program to look for lines of the form:

New Revision: 39772

Extract the number from each of the lines using a regular expression and the
findall() method. Compute the average of the numbers and print out the average
as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
'''

# import re
#
#
# hand =  open('mbox_short.txt', 'r')
#
# cnt = 0
# sum = 0
# for line in hand:
#     line = line.rstrip()
#     found = re.findall('^New Revision: ([0-9]+)', line)
#     for num in found:
#         num = int(num)
#         cnt += 1
#         sum += num

# print(sum//cnt)

import re

file_name = input("File name: ")
hnd = open(file_name, 'r')

nums = []
for line in hnd:
    line = line.rstrip()
    found = re.findall('^New Revision: ([0-9]+)', line)
    if found:
        nums.append(int(found[0]))  # because found is a list

print(sum(nums)//len(nums))



# import re

# hand =  open('regex_sum_42.txt')
# numlist = list()
# for line in hand:
#     line = line.rstrip()
#     stuff = re.findall('^\s ([0 - 9]+) \s', line)
#     if len(stuff) > 0:
#         print(stuff)
#     num = int(stuff[0])
#     numlist.append(num)
#
# print(sum(numlist))
# rgxp = input('Enter a regular expression: ')
# hand =  open('mbox.txt')
# # numlist = list()
# cnt = 0
# for line in hand:
#     line = line.rstrip()
#     if re.findall(rgxp, line):
#         cnt += 1
#     # if len(stuff) > 0:
#     #     print(stuff)
# #     num = int(stuff[0])
# #     numlist.append(num)
# #
# print(cnt)
