# Practice with Python Tuples
#  checking most common word on a file the return

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()

for k,v in counts.items():
    lst.append((v, k))

lst = sorted(lst, reverse=True)
for v, k in lst[0:10]:  # get only the top 10
    print(k,v)
