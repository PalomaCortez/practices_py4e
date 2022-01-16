# Practice with Python Tuples
# Tuples and dictionaries methods
# for loop
# if condition


'''
py4e book - 10.3: Write a program that reads a file and prints the letters in decreasing
order of frequency. Your program should convert all the input to lower
case and only count the letters a-z. Your program should not count
spaces, digits, punctuation, or anything other than the letters a-z.
Find text samples from several different languages and see how letter
frequency varies between languages. Compare your results with the
tables at https://wikipedia.org/wiki/Letter_frequencies.
'''

fhand = open('mbox_short.txt')
emails = dict()
for line in fhand:
    line = line.lower()
    for c in line:
        emails[c] = emails.get(c,0) + 1

freq = []
for ch, count in emails.items():
    if 'a' <= ch <= 'z':
        freq.append( (count, ch) )
# freq.sort()
#
# for ch, count in freq:
#     print (ch, count)
freq = sorted(freq, reverse=True)
for v, k in freq:
    print(k,v)

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
#
# lst = list()
#
# for k,v in counts.items():
#     lst.append((v, k))
#
# lst = sorted(lst, reverse=True)
# for v, k in lst[0:10]:  # get only the top 10
#     print(k,v)
