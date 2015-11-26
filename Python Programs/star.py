#!/usr/bin/env python

'''
*
**
***
****
*****
'''
n = int(raw_input("Enter the number of lines"))
for n in range (1, n):
    print "*" * (n)

'''
*****
****
***
**
*
'''
n2 = int(raw_input("Enter the number of lines"))
for n2 in range (n2, 0, -1):
#range prints from n2 to 0 where -1 is the step.
    print "*" * (n2)
