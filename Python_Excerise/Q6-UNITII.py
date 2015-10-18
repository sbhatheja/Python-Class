#!/usr/bin/python
__author__ = 'sbhatheja'

'''Write a program which accepts a string as input to print Yes if the string is "yes" or "YES" or "Yes", otherwise print

"No".

Hints:

Use if statement to judge condition.'''


u_input = raw_input("Enter a string:")
if u_input == 'yes' or u_input == 'YES' or u_input == 'Yes':
    print('Yes')
else:
    print('No')
