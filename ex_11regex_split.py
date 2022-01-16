# Practice with Python Regular Expressions
# how to get an email address from a string

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Procedure 1 - without RedEx

# words = line.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])


# Procedure 2 - RedEx

import re
y = re.findall('^From .*@([^ ]*)', line)
print(y)
