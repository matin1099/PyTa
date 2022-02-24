#VARIABLES: Section 1 "Python Variable"
'''
VARIABLES
Variables are containers for storing data values.
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
'''

x=15
y='abbas boazar'
print (x)
print(y)
'''
Variables do not need to be declared with any particular type, and can even change type after they have been set.
Sometimes we need to declare what type of a data we expect.
Like Blow
'''
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
msg1='remember our x and y above?'
print(type(x)) #expect int
print(type(y)) #expect str

#String variables can be declared either by using single or double quotes
y="abbas"
y='boazar'

# VARIAVLES ARE CASE SENSITVE
a='an var'
A="a Diffrent var"
