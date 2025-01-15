#Python Home 
print("Hello world")

#---------------------------------------------------------------------------

#Python get started
import sys

print(sys.version)

#--------------------------------------------------------------------------

#Python Syntax
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#--------------------------------------------------------------------------

#Pyhton comments 
print("Hello, World!") #This is a comment

#--------------------------------------------------------------------------

#Pyhton Variables 
#it is from "python variables"
x = 5
y = "John"
print(type(x))
print(type(y))

#it is from "Variable names"
my_variable_name = "John"
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#it is from "assign mulitpe values"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#it is from "output variables"
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#it is from "global variables"
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#-----------------------------------------------------------------------------

#Python Data Types 
x = 5
name = "Josh"
print(type(name))
print(type(x))

#------------------------------------------------------------------------------

#Python Numbers 
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
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#------------------------------------------------------------------------------

#Pyhton Casting 
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#------------------------------------------------------------------------------

#Pyhton Strings 
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)