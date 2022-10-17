# Flow Control

Flow control is one of the most important parts of programming. While being able to assign values is necessary to work with memory, flow control allows for the programmers to change the direction of a program based on events. `Conditionals` can chagne what is exactly exeecuted while `Loops` can execute the same code multiple times. 

There are 3 phrases that are thrown around a lot that might be useful to describe here: `Tautology`, `Condradiction`, `Contingency`.
- Tautology -> a statement that is always true
- Contradiction -> a statement that is always false
- Contingency -> a statement that is sometimes true, sometimes false

## Conditional Logic
There are things that are absolutes: murder is wrong, the IRS will find you, and programmers will fight over the 'best' language. However, there are also things that require a condition to occur: I will go to the park **if** it does not rain today. This `if` is a fundemental, and often overused, tool of the trade.

### If statement
The `if` statement, as described above, is used to re-direct the flow of a program execution. The `if` statement takes in a boolean value and can also hold computations inside of it. It can compare variables, values, and anything that anything is comparable.

There are several logical operators that can be used in these conditional comparisons. Here is a list of the most commonly used ones.

```
Logical AND -> and 
Logical OR -> or 
Logical NOT -> not 
Compare Equality -> (==)
Greater Than -> >
Greater Than or Equal to -> >=
Less Than -> <
Less Than or Equal to -> <=
```

```py
# Booleans
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
```

The combination of multiple `if` statements might be necessary sometime in order to create a combinational conditional statement. Let us see an example:

```py
# Let us check to see if our value is in between a specified range
a = 3
# Check if a is between 1 and 10
if a > 1:
    if a < 10:
        print('a is in range!')
```
This can be simplified using the `and` operation:

```py
# Same as before
a = 3
if a > 1 and a < 10:
    print('a is in range!')

# This can also be shortened into this form
if 1 > a > 10:
    print('a is in range!')
```
Another case would be if you were checking for two different cases. Imagine if we were to check if something was `not` in range. This could be done through several different methods. Below I will explore 2 different examples:
```py
a = 5

# negation
if not (1 > a > 10):
    print('a is not in range!')

# Check to see if out of range
if a < 1 or a > 10:
    print('a is not in range!')

# The parenthesis is used to tell the compiler what to evaluate first.
# It can also be used to bring readability to the code.
```
Both of these will return the same thing and can be explained through `De Morgan's Laws`. For this course, I will not be expanding on the concept.
### If-else
So what happens if you want to handle both sides of a case? This is where the phrase `else` comes from. Let us examine the idea of going to the park again.

`If` it is `not` raining today, I will go to the park. `Else` I will stay at home.

This is a commmon method of handling the flow of the program. It allows for only certain things to execute and is useful to handle **both** cases.

```py
raining = True

if not raining:
    print('I went to the park!')
else:
    print('I stayed at home!')
```
These can be chained together with multiple if conditions too in case you are handle several special conditions. This is done with the addition of the `elif` phrase for each additional `if`.
```py
raining = True
hungry = True

if not (raining and hungry):
    print('I went to the park!')
elif not raining and hungry:
    print('I went to the store!')
else:
    print('I stayed at home!')
```
The reason I said this was one of the most overused tools is because people will often continually chain `if-else` after `if-else`. Sometimes these are necessary, but other times they can be simplified. This comes down to experience and analyzing efficiency, which we will not be discussing in this course.
## Short Circuiting
`Short Circuiting` references the act of taking the path of least resistance. When your electronics 'short circuit', it means that there was something which caused a bypass over all the winds and turns that the electricity should have gone. This will cause the electronic to break, as the electricity goes at too high of a voltage and/or too high of a current where it should it not go yet.

In programming, we look to take the path of least resistance to speed up performance, without breaking our stuff of course.

Python's `and` and `or` are the short circuit operators. The way they work is:
```
and: evaluates the second term ONLY if the first term is True
or: evaluates the second term ONLY if the first term is False
``` 

As you can see, the first term is crucially important to whether the second term is even evaluated. Therefore, if you were to know that a certain expression were to be MORE influential in the overall statement than the other, that one should go first.

```
and -> the influential term would be the term that returns False 
or -> the influential term would be the term that returns True

This is because the `and` term will terminate if the first term is `False`

This is because the `or` term will terminate if the first term is `True`
```

While it does not necessarily matter at a small scale which term if the `if` statement goes first, it can save some time on a larger scale.

```py
# Short Circuit examples
if False and True:
    print('Not Reachable')
else:
    print('AND short circuit')
    
if True or False:
    print('OR short circuit')
```

### Ternary Operator
The ternary operator is a special case of the `if else`. It is a conditional statement that is more condensed than the `if else`.

```py
# Ternary
# x = 5, y = 6
x, y = 5, 6
# ternary operation
# 'x is larger' if x > y else 'y is larger'
print('x is larger' if x > y else 'y is larger')
```

## Switch
`Switch` statements are similar to if statements but function on a `case` basis. Unlike their `if` counterparts, they take in a value and figure which `case` to go to rather than testing for `True` or `False`. Python does not have a direct implementation of the `Switch` statement unlike other languages.

```cpp
// ... represents some action, whether that be print, calculating something, etc.
// C++ implementation
int variableName = 12;

// input is == 12
switch (variableName) {
    case 1: ... // if the input == 1
    case 2: ...
    case 3: ...
    default: ... // if none of the cases equal the input
} // switch
```
Python can use several methods to imitate this behavor, most commonly a `if-else` chain or a `dictionary`. While you have previously observed the `if-else`, dictionaries will be covered a bit later on in chapter 3.
```py
# python implementation
# following example from above
variable_name = 12

# if else chain
if variable_name == 1:
    ...
elif variable_name == 2:
    ...
elif variable_name == 3:
    ...
else: # default case
    ...

# Dictionary

switcher = {
    1:'number 1'
    2:...
    3:...
    ...
}
switcher.get(case)
# the .get(case) portion just pulls the left hand that relates to that 
# specific value
# example: .get(1) == 'number 1' 
```
Typically, dictionaries are used instead of the if chain as it makes the code more readable. 

## Loops
There are two major types of loops: `while` and `for`. The `while` loop is used when you do not know how many times you want to loop, but what `condition` you want to check for. A `for` loop is when you know how many times or you have a list you want to go through. 

### While
```py
while condition:
    event
```
While loops can be incredibly powerful when used for the right reason. One big issue is to not cause perpetual loops (the while condition always evaluates to True) or loops that never run (the while condition evaluates to False always).

 

```py
# Tautology
while True:
    print('This is Dangerous! Infinite Loop.')

# Contradiction
while False:
    print('This is not dangerous, just pointless. Never Runs!')

i = 0
while i < 100:
    print(i)
    i = i + 1
    # will print it out 100 times.
```
### For Loop

For loops can be in two different branches: `for-range`, and `for-each`. `For-range` is used if there is a given amount of values that need to be gone through. A good example would be when you are trying to count from 0 to 100. `For-each` loops takes this idea and applies it to a definite structure. If you have a list that needs to go over, the `for-each` is preferable.

The `for` loop, unlike the `while` loop, provides a variable which holds the iteration(which loop they are on) of the execution. For a `for-each`, this iteration variable is replaced with the list of values you supplied.

```py
# for range
for iteration in range(range_value):
    event

# collection of values
# for each
values = [...]
for variable in values:
    event
```
**Range**

To more clearly define the `range()` function, it generates a list of integers from 0 up to the value given. 

n = number input

list = 0, ... , n-1

```
Example:
range(5) = [0, 1, 2, 3, 4]
```

This is what we call **inclusive** and **exclusive** for our values. If I were to say that it goes up to 5 inclusive, it would go:

0, 1, 2, 3, 4, 5

The range function itself is **inclusive** for its lower bound (0) and **exclusive** for its upper bound (n). This is important to understand when working with functions or formulas that other people devise, as it will be easier to work with them.

```py
# Example:
for x in range(4):
    print(x)
    # 0, 1, 2, 3

values = [2, 4, 6, 8]
for x in values:
    print(x)
    # 2, 4, 6, 8
```

