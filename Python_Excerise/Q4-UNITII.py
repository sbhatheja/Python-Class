#!/usr/bin/python
__author__ = 'sbhatheja'

''' Write a script which works out how old a child should be to know a certain word. The classification should be based

on the length of the word, as follows:

5 years <= 3 letters

6 years <= 4 letters

8 years <= 6 letters

10 years <= 10 letters

12 years = any length'''


u_input = input("Enter the age of the child:")

if u_input <= 5:
    print("3 Letters")
elif u_input <= 6:
    print("4 Letters")
elif u_input <= 8:
    print("6 Letters")
elif u_input <= 10:
    print("10 Letters")
elif u_input == 12:
    print("Any words")


