# Practice with Python Dictionaries
# Histogram code

# Considering a sequence of item names given, how can we know the
# amount of each item?

# 1st we open a dictionary where the quantities will be stored
item_qty = dict()

# example of noums to be processed
items = ['ita', 'itb', 'itc', 'itn', 'itc', 'itn', 'itb']

# option 1:
# for item in items:
#     if item not in item_qty:
#         item_qty[item] = 1
#     else:
#         item_qty[item] += 1
#
# print(item_qty)

# option 2:
# for item in items:
#     item_qty[item] = item_qty.get(item, 0) + 1
#
# print(item_qty)

# option 3:
for item in items:
    item_qty[item] = item_qty.count(item)

print(item_qty)
