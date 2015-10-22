#!/usr/bin/python
__author__ = 'sbhatheja'

'''Assignment 1:

Input:
days = ['yesterday','today','tomorrow','dayafter']

Output:
Yesterday
TOday
TOMorrow
DAYAfter
'''

days = ['yesterday','today','tomorrow','dayafter','firstday']

for d_count in range(0,len(days)):
    day = days[d_count][0:d_count+1].upper()
    print(day + days[d_count][d_count+1:])



