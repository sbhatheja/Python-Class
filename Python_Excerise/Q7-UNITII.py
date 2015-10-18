#!/usr/bin/python
__author__ = 'sbhatheja'

'''Write a small password checking script. This will record the username, old password and new password. The rules

are that a password is OK if it is >7 characters long, contains some uppercase characters and is different to the old

password. The admin user (username 'admin') can do whatever they like. Print out whether the new password is OK.

Try doing this as one compound if statement'''


username = raw_input("Enter the username:")
o_passwd = raw_input("Enter the old password:")
n_passwd =  raw_input("Entet the new password:")

if n_passwd != o_passwd and len(n_passwd) > 7 and username != 'admin' and \
        not n_passwd.islower():
    print("New password is OK")
elif n_passwd == o_passwd:
    print("Both the passwors are same")
elif len(n_passwd) <= 7:
    print("Password should be 7 characters long")
elif  n_passwd.islower():
    print("Password should contains some uppercase characters")