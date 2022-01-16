# Practice with Python Files
# file methods
# string methods
# try/except
# for loop

'''
py4e 07_02: Write a program that prompts for a file name, then opens
that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
'''

file_name = input('Enter the file name: ')
try:
    fhand = open(file_name)
except:
    print('File cannot be opened:', file_name)
    quit()
count = 0
flt_tot = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    ref_line = line
    position = (ref_line.find(':') + 1)
    flt = float(ref_line[position: ])
    count += 1
    flt_tot = flt_tot + flt

print('Average spam confidence: ', flt_tot/count)
