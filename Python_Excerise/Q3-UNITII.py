#!/usr/bin/python
__author__ = 'sbhatheja'

'''Wap to find out if a given character is a vowel or consonant?'''

u_input = raw_input("Enter a character:")

if u_input in 'aeiou':
    print('vowel')
else:
    print('consonant')