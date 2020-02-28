# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:45:51 2020

@author: 212560141
"""
print ('hellow world')
print ("hellow world")
print ("""hellow world""")
print ('''hellow world''')

age = 20
name = 'Sandile'

print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
print('Hello World'[3:7])

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.
for i in range(0,100,5):
    print (i)