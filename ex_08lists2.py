# Practice with Python Lists
# open file
# for loop
# if condition
# list iterations

'''
py4e 08_05: Open the file mbox-short.txt and read it line by line.
for a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
parse the From line using split() and print out the second
word in the line (i.e. the entire address of the person who sent the
message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also
look at the last line of the sample output to see how to print the count. 
'''

fhand = open('mbox_short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
