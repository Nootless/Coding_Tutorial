# What is Python?
Python is a high level programming language that enables users to easily create software. Python focuses heavily on user readability, making it consistently one of the most preferred programming languages. It is commonly used in data science, image processing, machine learning, and many other applications. With hundreds of thousands different packages to develop applications along with its user friendly nature, it is a good entry point for aspiring programmers and computer scientists.
# Installing Python
Python can be installed through many different methods. Typically it is installed through the [Python website](https://www.python.org/). For the purposes of this tutorial, we will be working under the assumption you are using Python 3.0 or higher. Currently I am writing this while using 3.10.6. 
## Windows:
When installing it, make sure to install python for all users and add it to path. Adding Python to your paths will prevent future headache.
### Whoops!
If you accidentally did not add python to your paths when installing it, I would recommend going through [this](https://realpython.com/add-python-to-path/).
## Linux:
It can also be installed from the [Python website](https://www.python.org/) or from the methods below.

```py 
# Ubuntu (and Ubuntu based distributions)
sudo apt-get install python
# Arch (and Arch based distributions)
sudo pacman -S python
```
## Mac:
It can also be installed from the [Python website](https://www.python.org/).

## Recommended Software
You should be looking for a text editor or development environment to write your code. While there are tools such as notepad, vim, and emacs to write code, I would highly recommend a software which has more functionality for beginners. 
### Anaconda
[Anaconda](https://www.anaconda.com/) is one of the best software for data science. However, overall it is a solid choice. It comes with section code runnning for easier debugging. To start with, you must install either jupeyter lab or jupyter notebook.
### PyCharm
[Pycharm](https://www.jetbrains.com/pycharm/) is also a solid choice for python development. This software is is simple to use and very powerful.
### Visual Studio Code
[Visual Studio Code](https://code.visualstudio.com/) is a very easy to use text editor which can function as a code development center. It allows for several different workspaces to be held on the side. Additionally, addons can help assist in the development process as well as make code look nicer. For the documentation for installing, it can be found [here](https://code.visualstudio.com/docs/python/python-tutorial). 

# Hello, World!
One of the first projects (and the most exciting) is the Hello, World! program. To start writing programs, you must have a new file that ends in the extension name ``.py`` to let the python interpreter to know it's a python file (as well as for yourself!).

To begin with, we are going to create a file named ``main.py``. Typically this is the entry of your program and which functions as the 'driver' of your program.

```py
if __name__ == '__main__':
    print('Hello, World!')
```
While most of this might not be clear to a first time user, if ran this should output ``Hello, World!`` in the console. 

You probably have noticed that the line ``print('Hello, World!')`` is indented by a tab. Unlike C-like programming languages, Python does not use ``{}`` brackets to indicate constructions, but rather by indentation. While this might not make sense right now, it is important to start thinking about how python structures its code.

If there is any issues, please use google or directly ask me and I will post a running list of problems and solutions below.

