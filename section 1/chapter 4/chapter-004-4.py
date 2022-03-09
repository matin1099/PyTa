#VARIABLES: Section 3 "Output Variables"
'''

The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

'''

x = "LEGEND"
print("Zoghi is " + x)

#You can also use the + character to add a variable to another variable:

x = "Zoghi is "
y = "LEGEND"
z =  x + y
print(z)

#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

#If you try to combine a string and a number, Python will give you an error:
'''
x = 5
y = "John"
print(x + y)
'''
#Note: An important err! TypeError: unsupported operand type(s) for +: 'int' and 'str'