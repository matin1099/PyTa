#VARIABLES: Section 3 "Assign Multiple Values"
'''

Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
  
Note: Make sure the number of variables matches the number of values, or else you will get an error.

'''
a, b, c= "asghar","mamad","mostafa"
print(a)
print(b)
print(c)

#One Value to Multiple Variables
#And you can assign the same value to multiple variables in one line:

x = y = z = "sharbatoghli"
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)