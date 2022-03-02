#Python Data Types

# Built-in Data types
'''
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:  str
Numeric Types:  int, float, complex
Sequence Types: list, tuple, range
Mapping Type:   dict
Set Types:  set, frozenset
Boolean Type:   bool
Binary Types:   bytes, bytearray, memoryview

'''
#Getting the Data Type
#You can get the data type of any object by using the type() function:

x = 5
print(type(x))

#Setting the Data Type
#In Python, the data type is set when you assign a value to a variable:

x = "Hello World"   #str
print(x)
print(type(x))
x = 20  #int 
print(x)
print(type(x))
x = 20.5    #float   
print(x)
print(type(x))
x = 1j  #complex 
print(x)
print(type(x))
x = ["apple", "banana", "cherry"]   #list    
print(x)
print(type(x))
x = ("apple", "banana", "cherry")   #tuple   
print(x)
print(type(x))
x = range(6)    #range   
print(x)
print(type(x))
x = {"name" : "John", "age" : 36}   #dict    
print(x)
print(type(x))
x = {"apple", "banana", "cherry"}   #set 
print(x)
print(type(x))
x = frozenset({"apple", "banana", "cherry"})    #frozenset   
print(x)
print(type(x))
x = True    #bool    
print(x)
print(type(x))
x = b"Hello"    #bytes   
print(x)
print(type(x))
x = bytearray(5)    #bytearray   
print(x)
print(type(x))
x = memoryview(bytes(5))    #memoryview
print(x)
print(type(x))


print(7*"#")

#Setting the Specific Data Type
# very important for inputs
#If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")  #str 
x = int(20) #int 
x = float(20.5) #float   
x = complex(1j) #complex 
x = list(("apple", "banana", "cherry")) #list    
x = tuple(("apple", "banana", "cherry"))    #tuple   
x = range(6)    #range   
x = dict(name="John", age=36)   #dict    
x = set(("apple", "banana", "cherry"))  #set 
x = frozenset(("apple", "banana", "cherry"))    #frozenset   
x = bool(5) #bool    
x = bytes(5)    #bytes   
x = bytearray(5)    #bytearray   
x = memoryview(bytes(5))    #memoryview

