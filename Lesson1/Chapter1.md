# Chapter 1: Primitives, Variables, and Operations
Now that you have written your first program, you are officially a programmer! Even if you are not producing the next Facebook, everyone has to start somewhere. Before we start talking about developing programs, we must first understand the basics of how memory works. This chapter will mostly be theoretical and focus on the basic data structures.

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

## Variables and Constants

While other programming languages would require a variable initialization, Python will automatically determine the type of variable you have created. Variables are assigned through the ``=`` operator followed by a value. Taking from our original program, the ``Hello, World!``, we can store the message in a variable. 

```py
# Assignment 1

```

While understanding bits and bytes is important, being able to interact and apply these concepts is crucial for programmers.

## Booleans
A boolean is a ``True`` or ``False`` value. You can imagine it as a bit in this sense: 
```
True: 1
False: 0
```
All data types require ``bytes`` to store the information they contain. The ``boolean`` data type requires ``24 bits`` at a minimum, as it is different dependent on hardware requirements. To declare a boolean, python uses the keywords: ``True`` and ``False``.
> keyword: a word that have been defined by the programming language and have a signficant meaning/use


To assign these to a variable, we must first declare a name for said variable followed by the equals sign shown below: 
```pg
# foo and bar are both variables
foo = True
bar = False
```
## Integers


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