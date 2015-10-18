#!/usr/bin/python
__author__ = 'sbhatheja'
#log: version 1.0 created on 18th Oct
''' WAP to find the min of the two numbers ? '''

# Get the user input
num1 = input("Enter first number:")
num2 = input("Enter second number:")

# check for the minimum number
if num1 < num2:
    print("{} is minimum" .format(num1))
elif num1 == num2:
    print("Both numbers are equal")
else:
      print("{} is minimum" .format(num2))


