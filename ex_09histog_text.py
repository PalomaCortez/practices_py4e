# Practice with Python Dictionaries
# Histogram code - from a text

# Considering a text, how can we know the amount of each word?

# 1st we open a dictionarie where the quantities will be stored
word_qty = dict()
print('Enter the line of text: ')
line = input('')

# option 1:
# words = line.split()
#
# for word in words:
#      word_qty[word] = word_qty.get(word, 0) + 1
#
# print(word_qty)

# option 2:
for word in words:
     word_qty[word] = word_qty.count(word)

 print(word)
