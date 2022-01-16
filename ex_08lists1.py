# Practice with Python Lists
# open file
# for loop
# if condition
# list methods

'''
py4e 8.4: Open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split() method. The
program should build a list of words. For each word on each line check
to see if the word is already in the list and if not append it to the
list. When the program completes, sort and print the resulting words
in alphabetical order.
'''

fhand = open('romeo.txt')
line_list = list()
for line in fhand:
    ref_line = line.split()
    for i in range(len(ref_line)):
        if ref_line[i] not in line_list:
            line_list.append(ref_line[i])
line_list.sort()
print(line_list)
