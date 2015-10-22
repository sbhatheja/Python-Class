#!/usr/bin/python
__author__ = 'sbhatheja'

'''Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the

number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.'''

final_list = []

for num in range(1000, 3001):
    l = []
    if num % 2 == 0:
        for i in str(num):
            if not int(i) % 2 == 0:
                del l[:]
                break
            else:
                l.append(i)
        if not len(l) == 0:
            final_list.append("".join(l))
print(",".join(final_list))

