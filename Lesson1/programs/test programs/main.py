import sys
import math

# Testing for data sizes
# bool
print(f'bool size: {sys.getsizeof(True)}')

# int
print(f'int size: {sys.getsizeof(2)}')

# floats
print(f'float size: {sys.getsizeof(2.1)}')

# string
print(f'{type("string")} size: {sys.getsizeof("string")}')

# Operations

# Problem 1: Let us calculate a problem that you might not see very often
# but is a great introduction into using operators

# Let us say that you have a nozzle (converging diverging nozzle)
# to calculate for the mass flow rate through the nozzle you it is solved by
# m_dot = ro * v * A
# Assumptions
# Steady State, Isentropic, constant m_dot

# Define Variables
# m_dot = mass flow rate
# ro = density of fluid (in this case it is air)
# v = velocity
# A = area
# A = pi * r^2
# r = radius

# So to calculate m_dot, you would want to calculate everything

# Given values
r = 1 # in meters
ro = 1.2 # in kg / m^3
v = 200 # in m/s

# Area
area = math.pi * r**2

# calculate mass flow rate
m_dot = area * v * ro

# As you can see, it is much more readible to compute for multiple variables 
# rather than calculate it all at once.
# It also allows for the variables to be changed if you needed to calculate for
# a different m_dot or area.