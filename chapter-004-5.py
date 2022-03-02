#Global Variables
"""
Variables that are created outside of a function  (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

#create avariable outside of a function, and use it inside a function

x = "awesome" #Global Var

def myfunc():
  print("Python is " + x)

myfunc()

#Local Var: A variable that create inside of function ,class ,etc. ANYWHERE BUT MAIN CODE!!
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome" #Global Var

def myfunc():
  x = "fantastic" #Local Var
  print("Python is " + x)

myfunc() # work with Local

print("Python is " + x) #work with Global


#The global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x #declear This x is  Global every where we call x , we mean this x!
  x = "fantastic"

myfunc()

print("Python is " + x) #Work with Global var that located in a func!

#!!! DANGER ZONE !!!

#when we declear a var with global keyword , ANY CHANGES WILL BE GLOBAL!!!
x = "awesome"
print("x out side of func and x=" + x)
def myfunc():
  global x
  x = "fantastic"
  print("x in side of func and x=" + x)

myfunc()

print("Python is " + x)

