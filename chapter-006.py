#Python Numbers
"""
There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them:

"""
 #To verify the type of any object in Python, use the type() function:

x = 1    # int
print(type(x))
y = 2.8  # float
print(type(y))
z = 1j   # complex
print(type(z))

#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
print(type(x))
y = 35656222554887711
print(type(y))
z = -3255522
print(type(z))

'''Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.'''

x = 1.25
print(type(x))
y = 3565.6222554887711
print(type(y))
z = -32550.522
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
print(type(x))
y = 12E4
print(type(y))
z =  -87.7e100
print(type(z))

#Complex
#Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
print(type(x))
y = 5j
print(type(y))
z =  -5j
print(type(z))

#Type Conversion
#You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
#Bonus
#RANDOM
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))