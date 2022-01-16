# Practice with Python Loops and iterations
# input
# while loop
# if condition
# try / except

'''
py4e - 5.2: Write a program that repeatedly prompts a user for integer numbers
until the user enters 'done'. Once 'done' is entered, print out the largest
and smallest of the numbers. If the user enters anything other than a valid
number catch it with a try/except and put out an appropriate message and
ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
'''

largest = None
smallest = None
while True:
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        i_val = int(sval)
        if largest == None or smallest == None:
            largest = i_val
            smallest = i_val

        if largest < i_val:
             largest = i_val
        elif smallest > i_val:
            smallest = i_val

    except:
        print('Invalid input')
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
