#!/usr/bin/python
__author__ = 'sbhatheja'

'''Write a program that can receive two integral numbers in string form and compute their sum and then print it in

console.

Hints:

Use int() to convert a string to integer.'''

finput = raw_input("Enter first number:")
sinput = raw_input('Enter second number:')

sum = int(finput) + int(sinput)
print(sum)

