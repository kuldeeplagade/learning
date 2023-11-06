a="orange"
print(a[3])

print("orenge"[2])
#slicing
a="stringvalues"
print(a[:3])
print(a[1:3])
print(a[5:])
print("*******\n *****\n  ***\n   *")

#Input function
name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
 
print("So your name is " + name + ", your quest is " + quest + ", and your favorite color is " + color + ".")

a="kuldeep"
print(type(a))

#print() the sum of the integer they entered and 10.
use_int = int(input("Please enter an integer."))
 
print(use_int + 10)

#Difining a function
def function_name():
    print(2+2)
function_name()

#function with no parameter
def hello_world_printer():
    print("hello world")
 
 
hello_world_printer()

#function with one parmeter 
def name_printer(user_name):
    print(user_name)
 
 
name = input("Please enter your name.")
name_printer(name)
#volume of prisum
length = int(input("Enter an integer that represents length in feet."))
width = int(input("Enter an integer that represents width in feet."))
height = int(input("Enter an integer that represents height in feet."))
 
 
def prism_vol(l, w, h):
    return l * w * h
 
 
print("The volume of the rectangular prism is " + str(prism_vol(length, width, height)) + " cubic feet.")

#Celsius to Fahrenheit
celsius = int(input("Please enter an integer value for degrees celsius. "))
 
 
def fahrenheit(cel):
    return (18 * cel + 320) / 10
 
 
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")

import random

print(random.randint(1, 10))

#modules
from random import randint
fuel = randint(10, 25)
miles = randint(200, 400)
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
print("The car can travel " + str(miles) + " miles on a full tank.")



























