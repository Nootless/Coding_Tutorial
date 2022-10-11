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
```

Variables are important as they allow us to hold a specific ``state`` of something in the program and utilize them later on. 

### Constants
Constants, similar to their variable counterparts, do not have a specific declaration. Constants differ from variables as they do not change during the execution of the program. They are typically used to hold mathmatical constants like ``pi`` or ``e`` and program specific constants. The convention to declare a constant is all uppercase.
```py
# Constant
MY_NAME = 'Nootless'
``` 

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
# Strings
A [string](https://en.wikipedia.org/wiki/String_(computer_science) is a collection of characters, typically denoted as an alphabet. Python 3.0 supports [Unicode](https://en.wikipedia.org/wiki/Unicode) which is a standardization of representing characters.

## Data Type Sizes
The size of a data type is dependent on hardware. Below is a <b><u>MINIMUM</u></b> requirement for Python. 
```
Data Type   | Size
===================
Boolean     | 24
Integer     |
Float       |
String      |
 ```

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