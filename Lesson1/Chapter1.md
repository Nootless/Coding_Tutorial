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
A [string](https://en.wikipedia.org/wiki/String_computer_science) is a collection of ``characters``, typically denoted as an alphabet. Python 3.0 supports [Unicode](https://en.wikipedia.org/wiki/Unicode), which is a standardization of representing characters. These are the words that make up the tutorial you have been reading. The unique part of Unicode is that it includes all of [ASCII](https://en.wikipedia.org/wiki/ASCII) (American Standard Code for Information Interchage), which is all characters on your keyboard, <b>AND</b> worldwide languages and symbols. 

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
The size of a data type is dependent on hardware. Below is a <b><u>MINIMUM</u></b> requirement for Python. 
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

One operation that might be new to most people is the modulus operator. Dennoted with ``%``, it is used to get the <b>remainder</b> of the two. So think of it as a division where you use the remainder rather than discarding it. 

## Bitwise Operations
Bitwise operations is a fundemental part of computer science. While they are one of the fastest operations in any programming language, they are incredibly strange to work with when you first start. <b>DO NOT WORRY IF YOU DON'T UNDERSTAND THEM!</b> These are relatively complex operations that are rarely used by new and intermediate programmers. In this section I will be going to a binary representation of our numbers to make it easier to visualize.

### Bitwise shifting
``Bitwise shifting`` (bit shifting for short) is done by moving all binary bits by x amount, where x is the number input. There are two types of bit shifting operators: ``Left Shift`` and ``Right Shift``.

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

In a decimal system, if we were to 'shift' our place by 2 left, we would increase by 100 times (10 -> 1000). This is the same if we were to 'shift' our place by 2 right, it would decrease it by 1/100 times (10 -> 0). The reason the value is lost instead of becoming a decimal is because the bit 'disappears'.  
# Assignments
```py
# Assignment 1: Variable Assigning
# Assignment 2: Type Casting

```


# Questions
```
Question 1: How many bits would you need to represent 1000?

Question 2: How many bytes would you need to represent 1000?
```

# Answers
```
Question 1:
Answer: 10 bits
2^10 = 1024
Can represent up to 1024

Question 2:
Answer: 2 bytes
2^(8 + 8) = 2^16
Can represent up to 65536
```