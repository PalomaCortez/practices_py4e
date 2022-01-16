# Practice with Python Basics
# input
# if condition:
# try / except


    pass
number = 0
while 0 <= number < 6:
    number = int(input("Enter a number: "))
    try:
        if 0 <= number < 6:
            continue
        if number < 0 or number > 5:
            print("done")

    except:
        print("bad data")
        break
