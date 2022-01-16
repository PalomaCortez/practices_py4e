# Practice with Python Tuples
# Tuples and list methods
# for loop
# if condition


'''
py4e - 10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages. You can
pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the
counts, sorted by hour as shown below.
'''

fname = input('Enter file name: ')
try:
	fhand = open(fname)
except:
	print ('File cannot be opened:', fname)
	exit()
#fhand = open('mbox_short.txt')
emails = dict()
for line in fhand:
    if line.startswith('From '):
        line = line.split()
        ref = line[5]
        ref = ref.split(':')
        time = ref[0]
        emails[time] = emails.get(time,0) + 1

freq = list()
freq = sorted([(k, v) for k, v in emails.items()])

for k, v in freq:
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
