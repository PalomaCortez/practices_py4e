# Practice with Python Regular Expressions

# py4e - autograder chapter 11

import re

file_name = input('Enter file name: ')
handle = open(file_name, 'r')
#
# nums = []
# cumulus = 0
# for line in handle:
#     line = line.rstrip()
#     num = re.findall('[0-9]+', line)
#     if num:
#         for n in num:
#             nums.append(int(n))
# file_name =
# print(sum([int(x) for n in re.findall('[0-9]+', 'regex_sum_1432983.txt'.read())]))

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
