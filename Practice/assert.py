#!/usr/bin/python3.5
'''
When a program is correct, all of the assertions are true no matter what inputs are provided. When a program has an error, at least one assertion winds
up false for some combination of inputs. Python directly supports assertions through an assert statement.
There are two forms:
assert condition
assert condition , expression
'''
max= 0
a = input('Write a number \n')
b = input('Write some another number \n')
if a < b: max= b
if b < a: max= a
assert (max == a or max == b) and max >= a and max >= b

'''
Run this program with a equal to b and not equal to zero; it will raise the AssertionError exception. Clearly, the if statements don't set max to the
largest of a and b when a = b. There is a problem in the if statements, and the presence of the problem is revealed by the assertion.
'''
