# Chapter 1: Primitives, Variables, and Operations
Now that you have written your first program, you are officially a programmer! Even if you are not producing the next Facebook, everyone has to start somewhere. Before we start talking about developing programs, we must first understand the basics of how memory works. This chapter will mostly be theoretical and focus on the basic data structures. I encourage you to try everything that is displayed in code blocks to test your knowledge. At the end of the chapter, a set of questions and projects will be discussed.

## Memory Allocation
The fundemental point of storage we work with is called the [bit](https://en.wikipedia.org/wiki/Bit). The bit can only store information on if it was ``on: 1`` or ``off: 0``. While this seems limited, this is the fundemental building block of all of modern computing. These bits can be combined together to represent numbers, also known as the ``binary`` system. Below is a basic representation of how numbers in the ``decimal`` system can be represented in the ``binary`` system. 
```py
Decimal | Binary
0       | 0
1       | 1
2       | 10
3       | 11
4       | 100
5       | 101
...     | ...
10      | 1010
``` 

Each additional digit place for a binary bit adds an additional 2<sup>n</sup> digits, so:
```
Example:
# bits can carry either 1 or 0
1 bit = (0)

For 3 binary bits (0)(0)(0):
2^3 = 2 * 2 * 2 = 8 
For 5 binary bits (0)(0)(0)(0)(0):
2^5 = 2 * 2 * 2 * 2 * 2 = 32
```

The more commonly used unit is the [byte](https://en.wikipedia.org/wiki/Byte). You might have heard of these over bits, as ``bytes`` are used to measure how much space files take up on your storage. Bytes are made up of 8 bits, and can be used to represent 256 values. They also can be combined together similarly to bits, but must be in 2<sup>8</sup> increments.


```
Example:
1 bit = (0)
1 byte = (00000000)
For 3 bytes (00000000) (00000000) (00000000):
2^(8 + 8 + 8) = 16777216
```

While understanding bits and bytes is important, being able to interact and apply these concepts is crucial for programmers.

## Commenting and Code Style
One of the most important  parts of programming is making sure your program works. However, making it human readable is equally if not more important. While this section could have been placed anywhere, it is important to understand it sooner rather than later.

### Commenting
To comment on your beautiful code, preface your statement with a ``#`` for a single line comment, or ``""" """`` for a multiple line comment.

```py
# This is my comment!
name = 'Nootless' # it can also be placed in the same line

""" This is how you would write a multiline comment!
Usually it is not used as multiple one line comments are preferred. """

```

> "Where should I comment?" - ConcernedCoder21

While new programmers love to comment everything (I was there once), you should NOT comment on every line. Instead, comments should be used to explain harder lines of code and a general description of code blocks. 

Another way to make your code more readable is having a consistent coding style and naming your variables properly.

### Naming Conventions
Typically most people prefer to follow the [Python Style Guide](https://peps.python.org/pep-0008/), which is a set of standards of how to make code readable. While I highly suggest utlizing this as a tool so that your code is readable by other programmers, one of the core tenants is:

> A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.

So if you have a consistent coding style (that is readable), do not worry too much about following the guide one to one. In this course, my convention will be as follows:

```py
# Comments will have a space after the #

# Variables and functions
# lowercase
# Snake Case -> every_word_is_separated_by_underscore
foo_bar = ...

# Classes
# Capitalized
# PascalCase -> AllWordsAreCapitalizedAndNotSeparated
My_Class()
```
Do not worry if you do not fully understand! As we go through a few more examples it will become much more clear.

## Variables and Constants

While other programming languages would require a variable initialization, Python will automatically determine the type of variable you have created. Every variable has a type which python determines based on context and what is assigned.

### Variables
```cpp
// C++ 
int age = 20;
```
```py
# Python
age = 20 
```
Above, it can be seen that python will accept the variable declaration ``age = 20`` even though it was not explicitly declared by the user to be an integer. We will be going more into depth about what exactly an integer is in the next section.

Variables are assigned through the ``=`` operator followed by a value. Taking from our original program, the ``Hello, World!``, we can store the message in a variable:

```py
# Original:
if __name__ == '__main__':
    print('Hello, World!')

# Adjusted:
if __name__ == '__main__':
    greeting = 'Hello, World!'
    print(greeting)

# Would print same message
```

Variables are important as they allow us to hold a specific ``state`` of something in the program and utilize them later on. 

### Constants
Constants, similar to their variable counterparts, do not have a specific declaration. Constants differ from variables as they do not change during the execution of the program. They are typically used to hold mathmatical constants like ``pi`` or ``e`` and program specific constants. The convention to declare a constant is all uppercase.
```py
# Constant
MY_FAVORITE_NUMBER = 1
``` 

# 1. Data Structures
Fundementally, a data structure is just a way of storing information, whether that be words, numbers, collections of data, and so on. In this section, we will be discussing the fundemental data structures, known commonly as ``Primitive Types``.
## Booleans
A boolean is a ``True`` or ``False`` value. You can imagine it as a bit in this sense: 

```
True: 1
False: 0
```

All data types require ``bytes`` to store the information they contain. To declare a boolean, python uses the keywords: ``True`` and ``False``.
> keyword: a word that have been defined by the programming language and have a signficant meaning/use


To assign these to a variable, we must first declare a name for said variable followed by the equals sign shown below: 
```py
# foo and bar are both variables
foo = True
bar = False
```
## Integers
An [integer](https://en.wikipedia.org/wiki/Integer) includes 0, all positive natural numbers(1, 2, 3, ...) and all negatives of the natural numbers(-1, -2, -3, ...). In a more simpler way, any whole number (no fractions!). Integers are commonly used in math, ``indexing``, and ``enumerations``. Hopefully you have heard of the first concept, but the other two will be covered later in the course. 

```py
integer_value = 0
negative_integer_value = -26
positive_integer_value = 10
```

## Floats
A [float](https://en.wikipedia.org/wiki/Floating-point_arithmetic) is an approximation of a fractional value, the implementation of which is out of the scope of this course. All that needs to be understood is that floating point values are:
```
1. A representation of fractional values
2. Are stored in terms of bits, which may cause small arithmetic errors
```
```py
floating_point_value = 24.5
```   
## Strings
A [string](https://en.wikipedia.org/wiki/String_computer_science) is a collection of ``characters``, typically denoted as an alphabet. Python 3.0 supports [Unicode](https://en.wikipedia.org/wiki/Unicode), which is a standardization of representing characters. These are the words that make up the tutorial you have been reading. The unique part of Unicode is that it includes all of [ASCII](https://en.wikipedia.org/wiki/ASCII) (American Standard Code for Information Interchage), which is all characters on your keyboard, **AND** worldwide languages and symbols. 

When declaring a string, it must be done inside single or double quotes. 
```py
my_name = 'Nootless'
```

Additionally, formatted strings can be used to create strings which are made up of a different variable and the string.
```py
my_name = 'Nootless'
statement = f'My name is {my_name}'

# statement 
# My name is Nootless
```
### Characters
A character is the base unit that makes a string. A character can be considered a string, but not all characters are strings. In other programming languages, a ``char`` (character) would be considered a separate data structure, but Python is built on strings. Therefore, character arithmetic will be omitted for this tutorial.
## Data Type Sizes
The size of a data type is dependent on hardware. Below is a **MINIMUM** requirement for Python. 
```
Data Type   | Size
===================
Boolean     | 24
Integer     | 24
Float       | 24
String      | Variable
 ```

The size of strings are variable dependent on the length of the string. This can be tested using the main file provided in the test programs.

## Void
Void is more of an abstract idea than the previous few. It is used to represent the existence of nothing and typically can be used for error handling and initialize empty variables (covered more in scope section). In Python 3.0, the keyword ``None`` is used to denote a void type object. While typically not used at an entry level, it is important to know of its existence for bug fixing.

## Implicit Type Casting vs. Explicit Type Casting
So far we have been working with exclusively implicit type casted values, but what is type casting? 

``Type Casting`` is how the data type of a variable is chosen. Integers being stored need to be of data type ``int``, strings need to be of type ``string`` and so on. What happens when there are issues with how Python interprets your data types or you need to change them explicity?

That's where explicit type casting comes into play! Other languages (C, C++, Java, ...) utilize this by default, but for the sake of simplicity and readability, Python does not. Below is two examples of explicit type casting.

```py
# Example 1: basic integer casting
var1 = 10
var2 = 3.1 # I want this value to be an integer
var2 = int(var2) # reassigns the integer version of var2 to var 2

# var2 before reassignment -> 3.1 | type -> float
# var2 after reassignment -> 3 | type -> int

# Example 2: Reading in numbers

# We will discuss this later, but just know that 
# input_value takes in user input
integer_input_value = input()
int_value = int(integer_input_value)

# User inputs: 3
# integer_input_value -> '3' | type -> string
# int_value -> 3 | type -> int
```
As you can see from above, there can be variables that have different types but seem to have the exact same inputs, notable in example 2. This is especially important when we move into the next section: operations. Issues with types can cause entire programs to fail.

# 2. Operators

``Operators`` are functions that are built into the Python language. Most of us use them on a daily basis. Monitoring your finances, using a calculator, and/or figuring out how long ago you ate: all of these are done using operators.

```
List of Basic Operators
+, addition
-, subtraction (negative addition)
*, multiplication
/, division
%, modulus
**, exponent 
```

Below is an example of how all these operators are used. All of these are stored in a variable, however you do not have to store them in a variable. If I were to ``print(1+1)``, it would still print out 2. 

```py
add = 1 + 1 # 2
subtract = 1 - 1 # 0
mult = 2 * 3 # 6
div = 3 / 3 # 1
mod = 5 % 3 # 2
expo = 2 ** 3 # 8
```

One operation that might be new to most people is the modulus operator. Dennoted with ``%``, it is used to get the **remainder** of the two. So think of it as a division where you use the remainder rather than discarding it. 
## Float and Integer operations
The difference between a float and an integer is its ``priority``. In terms of how we usually think about ints and floats is that they are the same thing but with different precisions. However, the compilers do not think that way. All integers are floats, but not all floats are integers (Integers are a subset of floats). For instance:
```
1 can be a floating point and an integer
1.01 can be a floating point but not an integer
```
As a result, integers are therefore converted into floats whenever there is an operation involving both.
```py
1 + 1 = 2 # int + int = int
1.0 + 1 = 2.0 # int + float = float
1.0 + 1.0 = 2.0 # float + float = float
```
While this usually will not cause issues, keep in mind ``precision`` errors. 
```py
# Precision Error
precision_err = 1.000001

# Testing equality 
1.000001 + 1 > 2 # Greater than 2 because of small fraction

```
In these cases, we need to round() or type cast the value into an ``integer``.

## Bitwise Operations
Bitwise operations is a fundemental part of computer science. While they are one of the fastest operations in any programming language, they are incredibly strange to work with when you first start. **DO NOT WORRY IF YOU DON'T UNDERSTAND THEM!** These are relatively complex operations that are rarely used by new and intermediate programmers. In this section I will be going to a binary representation of our numbers to make it easier to visualize.

### Bitwise shifting
``Bitwise shifting`` (bit shifting for short) is done by moving all binary bits by x amount, where x is the number input. Bit shifting is often used as a faster version of multiplicaiton and division. There are two types of bit shifting operators: ``Left Shift`` and ``Right Shift``.

```
Left Shift: <<
Right Shift: >>
```
```py
Example:
# Let us bitshift by 2 right and left on the number 6
# 6(decimal) -> 110(binary)

# Left Shift
# 110 -> 11000 (binary)
# 6 -> 24
left_shift = 6 << 2

# Right Shift
# 110 -> 1 (binary)
# 6 -> 1 (decimal)
right_shift = 6 >> 2
```
As you might have noticed, when the binary bits are shifted to the left, the value increases while it decreases when shifted right. 

In a decimal system, if we were to 'shift' our place by 2 left, we would increase by 100 times (10 -> 1000). This is the same if we were to 'shift' our place by 2 right, it would decrease it by 1/100 times (10 -> 0). Since our system is entirely in binary (computer bits), when we shift we multiply and divide by 2 respectively. 
> Bit shifting can be very useful when trying to work with powers of 2.

However, the reason the value is lost instead of becoming a decimal is because the bit 'disappears'. Put another way, think about bits like a set of buckets: When the buckets are filled with water (@), and when they are empty (_):
```
Floor \_/ \_/ \@/ \@/ Floor

-> Dump water right by 1

Floor \_/ \_/ \_/ \@/ Floor
```
When the buckets have water, and you can freely dump water between each other. However, if you decide to dump water onto the floor with no bucket, the water will not be kept (but the floor will be all wet!). Keep in mind while shifting left will usually lead to higher numbers, it also has a similar issue of losing values if you shift beyond what Python is stores them as (24 bytes for int).


### Bitwise Operators

For the last part of this chapter we will be discussing bitwise functions. There are four total:
```
Operator | Symbol
==================
Bit AND  | &
Bit OR   | |
Bit NOT  | ~
Bit XOR  | x ^ y
```
In this section I will showing the ``Truth Tables`` for ``AND``, ``OR``, ``NOT``, and ``XOR``. These are just ways of displaying what value you will get when doing the operation with which bits. ``NOT`` is a bit special since it is a ``unary`` operator, meaning it only uses a single value rather than two to perform operations

Let X and Y be two bits being operated on ``X _ Y = __``
```
     X & Y
      AND
===============
X   Y   | Value
0   0   |   0
0   1   |   0
1   0   |   0
1   1   |   1 
-> AND returns a 1 if both bits are 1
```
```
      X | Y
       OR
===============
X   Y   | Value
0   0   |   0
0   1   |   1
1   0   |   1
1   1   |   1 
-> OR returns a 1 if any bit has 1
```
```
   ~X 
   NOT
============
X   | Value
0   |   1
1   |   0 
-> NOT returns the opposite of its input
```
```
      X ^ Y
       XOR
===============
X   Y   | Value
0   0   |   0
0   1   |   1
1   0   |   1
1   1   |   0 
-> XOR returns a 1 if only one bit is 1
```

### Applications of Bitwise operators
Previously we have discussed the uses for bit shifting but how can bit manipulation help us?

> Storing booleans

Since each bit can be thought of as a separate boolean value, you can easily store many dozens of boolean values inside one integer value. 

Lets say that I have an integer `11001`. This is said to hold the boolean values for whether or not someone in the family has paid their taxes (beware the IRS). So from left to right we might have {Dad, Mom, Sister, Brother, Me}. If wanted to access my boolean value, all I would have to do is take the modulus 2 of the current integer.
```
11001 % 2 = 1 
-> This represents `True`, meaning that I have paid my taxes :)
```
Let us say we wanted to make sure our brother does not get carted away for tax fraud. To perform this we need to bit shift right by 2, skipping over sister and me. Then taking the modulus.
```
11001 >> 2 = 00110
00110 % 2 = 0
-> This represents `False`, meaning that brother needs to pay up :(
```

This is a relatively simple example and often times booleans are not shifted this way to improve readability of code (at the cost of significantly more memory).
There are other uses for bitwise operators, but these are outside the scope of this tutorial. If you do wish to learn more about bitwise manipulation, I would suggest a course more specifically in C, C++, and/or systems programming.

# Questions
```
Bits and Bobs
Question 1: How many bits would you need to represent 1000?
Question 2: How many bytes would you need to represent 1000?

Data Types
Question 3: How would I add the value 10 to '10'?

Question 4: How would I have Python interpret the number 15 as a floating point?

Bitwise Operations
```

# Answers
```
Question 1:
Answer: 10 bits
2^10 = 1024

This is because when you have bits, they each can represent 2 numbers: 0,1. Each bit you add introduces: 

2^n - 2^(n-1)

where n is the number of bits added together.
So to represent 1000, we need to use the logarithm. 

log2(1000) = 9.96578...

The use of a logarithm is not necessary, but it makes our lives much easier. The logarithm function is used to find the exponent for its base value (2).

Alternatives: 
Keep dividing by 2 until you get to 1, remove any decimals. 
1000 / 2 = 500 -> 1
500 / 2 = 250  -> 2
250 / 2 = 125  -> 3
125 / 2 = 67.5 -> 4
67 /2 = 33.5   -> 5
33 / 2 = 16.5  -> 6 
16 / 2 = 8     -> 7
8 / 2 = 4      -> 8
4 / 2 = 2      -> 9
2 / 2 = 1      -> 10

While this works, it is much longer.

Question 2:
Answer: 2 bytes
2^(8 + 8) = 2^16
Can represent up to 65536

Similar to our previous answer, we need to think of how much can each byte represent. As noted before, it takes 10 bits (2^10) to represent 1000. Recalling that a byte is a shorthand to represent 8 bits, we need to have ATLEAST 10 bits. In terms of multiples of 8:

8 * 1 = 8 bits < 10 bits
8 * 2 = 16 bits >= 10 bits

It can be seen that it requires 2 bytes, even though it goes almost 6 bits over (16 - 10 = 6). Keep in mind that you want to take the ceiling (rounding up) of whatever your value is.

Question 3:
You must type cast int('10') or float('10') in order to make it into a form acceptable by the operator '+'.

Question 4:
I would change 15 to 15.0 as the '.0' would tell Python's interpreter that you want it to be a floating point value.
```