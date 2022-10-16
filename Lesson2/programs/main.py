
# Conditional Logic
if True:
    print('This statement will always print')

if False:
    print('This statement will never print')

# Variable declaration
a = 10
b = 9

# Comparison
if 1 < 2:
    print('This will print since 1 is less than 2')

if 1 == 1:
    print('This will print since 1 is equal to 1')

if a < b:
    print('This statement will not print since 10 is not greater than')

# Let us check to see if our value is in between a specified range
a = 3
# Check if a is between 1 and 10
if a > 1:
    if a < 10:
        print('a is in range!')


# Same as before
a = 3
if a > 1 and a < 10:
    print('a is in range!')

# This can also be shortened into this form
if 1 > a > 10:
    print('a is in range!')

a = 5

# negation
if not (1 > a > 10):
    print('a is not in range!')

# Check to see if out of range
if a < 1 or a > 10:
    print('a is not in range!')

# The parenthesis is used to tell the compiler what to evaluate first.
# It can also be used to bring readability to the code.

# Testing out else

raining = True

if not raining:
    print('I went to the park!')
else:
    print('I stayed at home!')
