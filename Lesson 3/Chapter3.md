# Functions, Classes and Objects
Now that we have talked about basic data types, flow control, and have done some basic project programming, we will focus on how to *group* these ideas together. First, a few definitions:

`Function` - A set of code which aims to perform a task.

`Class` - A template for a collection of related functions and data members.

`Object` - An instance of a Class.

So that is quite a lot to take in, but we will expand on these concepts throughout this chapter. Before we discuss *how* to use these tools, we will discuss a fundemental relation known as `scope`.

## Scope
`Scope` is an idea which focuses on where a variable, object, function, etc. is **declared** and where it can be **used**.

> Review: Declaration is where a variable is defined

`Scope` is a relatively abstract idea, but it is also just as straightforward when understood. 

Think about the way that you would distribute security levels in a company. The new guy who has questionable reasons for being here is not getting top-secret access, and the owner should not be locked out of getting into the bathroom (except during cleaning). Scope works similarly by giving some variables more 'power' than others. Below is an example:

```py
# global variables
var1 = 'foo'

def my_function():
    var2 = 'bar'
    print('Prints Something')

if __name__ == '__main__':
    print('This is the main function')

    if var1 == 'foo':
        print('This would work')
    if var2 == 'bar':
        print('This would cause a runtime error!')
```
In this example, you can see both `global` and `local` scope.

`Global` scope is used to describe the highest scope. There can only be one and it is commonly thought of as variables that are accessible by everything. 

In this case, there are is a global variable : `var1` and a global function: `my_function`. These are because they are defined outside of the `main` statement, which is used to define the `entry point` of the application. This will be further elaborated on. 

`Local` scope is used to describe a subset of the `global` scope. Each variable in a local scope is attached to its specific function, class, object, etc.. These variables and functions can only be accessed by those that are 'lower' in scope or those of the same scope. 

In the above example, `var2` is a local variable of the `global` function `my_function`. If there was any variables in `main`, they would also be local to `main`.

Another way to think about these is this:

```
[Local scope (Global Scope)]
Everything is in the global scope box, but only local scope is in the local scope box. Everything in global scope can be used by local, but not all local can be used in the global.    
```
The discussion on *where* variables can be used and *where* they need to be declared is hard to visualize just in words, examples will make this much clearer. Do not worry! This is harder to grasp when you have not seen any actual code for it, so this chapter will have some coding examples to tie together the past 3 chapters now that you have some good background.

Since programs are read from top down, you also can not define a variable *before* you use it. You probably already have realized this in previous examples, but this point is important to stress now that we are moving forward with harder topics. 

# Functions
Functions are one of the core tools used for recycling code along with `for` loops and `while` loops. It also allows you to encapsulate code in to a more readable format. You already have utilized several different functions without realizing it: `print()`, `input()`, and `__main__`. We are focusing more on *user-defined* functions in this chapter and will be discussing external functions later on.

```cpp
returnType functionName(dataType varName, dataType varName2) {
    behavior
    return ...
} // functionName
```
```py
# python
def function_name(paramater_name, parameter_name2,...):
    behavior
    return ...
```
The above is how you define a function in Python and C++ for reference. Everything under the scope of a function must be indented by one indent. Every subsequent `if`, `for`, function, loop, or any thing that is under the scope of something else must have an indent.

```py
# Example:

if __name__ == '__main__':
    print('Hello')
    for x in range(5):
        if x == 0:
            print('Hello! First print!')
        print(f'Counting: {x}')
```
So this is a bit of a messy piece of code, but let us break it down step by step. Starting out, everything is under the scope of `main` in this program, meaning it must be indented by one to show it is 'contained' in `main`. Going further, the print is under the scope of `main`, as well as the `for` loop. Since `print` does not have anything underneath it, since it is just a function being called. Following this, underneath the `for` loop we have the `if` statement and the **third** overall print statement, not the second. Because there is no indent on the second print, it falls directly under the `for` loop. Lastly, under the `if` we have the second `print` statement. This will be broken down into a tree for simplicity.
```
Global Scope

`- main function
 |
 `- print('Hello')
 `- for x in range (5)
  |
  |`- if x == 0
  | |
  |  `- print('Hello! First print!')
  |
  `- print(f'counting: {x}')
```
Each branch

## Main function
The main function, as previously defined, is the 'entry point' of the application. This means that this is where Python


5. Functions, Classes, and Objects
    - Scope
    - Functions
    - Classes
        - Objects
        - class functions
            - Regular
            - Static