#!/usr/bin/python
__author__ = 'sbhatheja'

'''Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123

Then, the output should be:

LETTERS 10 DIGITS 3
Hints:

In case of input data being supplied to the question, it should be assumed to be a console input.'''

u_input = raw_input("Please enter a sentence:")

dcount = 0
lcount = 0

for val in u_input:
    if val.isalpha():
        lcount += 1
    elif val.isdigit():
        dcount += 1

print("LETTERS {} DIGITS {}".format(lcount,dcount))



