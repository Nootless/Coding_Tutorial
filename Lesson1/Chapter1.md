# Variables and Operations
Now that you have written your first program, you are officially a programmer! Even if you are not producing the next Facebook, everyone has to start somewhere. Before we start talking about developing programs, we must first understand the basics of how memory works.

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
```py
Example:
# bits can carry either 1 or 0
1 bit = (0)

For 3 binary bits (0)(0)(0):
2^3 = 2 * 2 * 2 = 8 
For 5 binary bits (0)(0)(0)(0)(0):
2^5 = 2 * 2 * 2 * 2 * 2 = 32
```
Quick quiz to see of you were paying attention! (Answers will be found at the end of the doc)
```
Question 1: How many bits would you need to represent 1000?
```


The more commonly used unit is the [byte](https://en.wikipedia.org/wiki/Byte). You might have heard of these over bits, as ``bytes`` are used to measure how much space files take up on your storage. Bytes are made up of 8 bits, and can be used to represent 256 values. They also can be combined together similarly to bits, but must be in 2<sup>8</sup> increments.

```
Example:
1 bit = (0)
1 byte = (00000000)
For 3 bytes (00000000) (00000000) (00000000):
2^(8 + 8 + 8) = 16777216
```

```
Question 2: How many bytes would you need to represent 1000?
```
While understanding bits and bytes is important, being able to interact and apply these concepts is crucial for programmers.
## Booleans
A boolean is a ``True`` or ``False`` value. You can imagine it as a bit in this sense: 
```
True: 1
False: 0
```

## Integers


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