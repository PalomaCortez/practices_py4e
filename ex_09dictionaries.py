# Practice with Python Dictionaries
# dictionaries methods
# read file
# for loop
# list methods

'''
py4e - 9.4: Write a program to read through the mbox-short.txt and figure
out who has sent the greatest number of mail messages. The program looks
for 'From ' lines and takes the second word of those lines as the
person who sent the mail.
The program creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the
dictionary using a maximum loop to find the most prolific committer.
'''

fhand = open('mbox_short.txt')
l_words = list()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    l_words.append(words[1])

word_qty = dict()
for word in l_words:
    word_qty[word] = word_qty.get(word, 0) + 1

# most = None
# prol = None
# for key in word_qty:
#     if most is None:
#         most = word_qty[key]
#     if (word_qty[key]) > most:
#         most = word_qty[key]
#         prol = key
#
#
# print(prol, most)

# Review for exercise 10.1
lst = list()
lst = sorted([(v, k) for k, v in word_qty.items()], reverse=True)

for v, k in lst[0:10]:  # get only the top 10
    print(k,v)
