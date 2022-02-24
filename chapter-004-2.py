#VARIABLES: Section 2 "Variable Names"
'''
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
    1- A variable name must start with a letter or the underscore character
    2- A variable name cannot start with a number
    3- A variable name can only contain Latin alpha-numeric characters and underscores (A-z, 0-9, and _ )
    4- Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

#Some legal var name:
myvar = "ahmad"
my_var = "ahmad"
_my_var = "ahmad"
myVar = "ahmad"
MYVAR = "ahmad"
myvar2 = "ahmad"

"""
ILLEGAL var name:
2myvar = "John"  =>  Start with number
my-var = "John"  =>  Use dash Non alpha-numeric
my var = "John"  =>  Use space! Non alpha-numeric
"""


#DID YOU KNOW??
'''Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:
'''
#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "Zoghi"

#Pascal Case
#Each word starts with a capital letter:

MyVariableName = "Zoghi"

#Snake Case
#Each word is separated by an underscore character:

my_variable_name = "Zoghi"