#!/usr/bin/python
__author__ = 'sbhatheja'

'''Write a program that computes the net amount of a bank account based a transaction log from console input. The

transaction log format is shown as following:

D 100 W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100

Then, the output should be: 500

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.'''


current_amount = 0
deposit = []
withdrawal = []

u_input = raw_input("Please enter the amount and amount type:")

count = 0
a = u_input.split(' ')
print(a)
for count in range(0, len(a)):
    if a[count] == 'D':
        count = count + 1
        deposit.append(a[count])
    elif a[count] == 'W':
        count = count + 1
        withdrawal.append(a[count])

sum_total = sum(int(i)for i in deposit) - sum(int(i)for i in withdrawal)
print(sum_total)