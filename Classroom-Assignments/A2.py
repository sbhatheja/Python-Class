#!/usr/bin/python
__author__ = 'sbhatheja'

'''Assignment 2:
Input
names = ['jhanvi','naresh','sunny','santo','jena','brahma','sri','brahma','sunny','naresh']

Output
finallist = ['jhanvi','naresh','sunny','santo','jena','brahma','sri']
dumplicated = ['brahma','sunny','naresh']'''

names = ['jhanvi','naresh','sunny','santo','jena','brahma','sri','brahma','sunny','naresh']

duplicated = []
finallist = []
for name in names:
    if names.count(name) > 1:
        names.remove(name)
        duplicated.append(name)

finallist = names
print("finallist = {}".format(finallist))
print("duplicate = {}".format(duplicated))


