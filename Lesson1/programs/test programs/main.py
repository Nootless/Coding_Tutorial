import sys

# bool
print(f'bool size: {sys.getsizeof(True)}')

# int
print(f'int size: {sys.getsizeof(2)}')

# floats
print(f'float size: {sys.getsizeof(2.1)}')

# string
print(f'{type("string")} size: {sys.getsizeof("string")}')
