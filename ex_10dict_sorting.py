# Practice with Python Tuples
#How to sort a dictionary

# d = {'a':10, 'b':1, 'c':22}
# d.items()
# for k,v in sorted(d.items()):
#     print(k,v)

#  checking most common word
# c = {'a':10, 'b':1, 'c':22}
# tmp = list()
#
# for k,v in c.items():
#     tmp.append((v, k))
# print(tmp)
#
# tmp = sorted(tmp, reverse=True)
# print(tmp)

# short version
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v, k) for k, v in c.items()]))
