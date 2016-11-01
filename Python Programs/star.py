#!/usr/bin/python3.5
'''
*
**
***
****
*****
'''
n = int(input("Enter the number of lines"))
for n in range (1, n):
    print ("*" * n)

'''
*****
****
***
**
*
'''
n2 = int(input("Enter the number of lines"))
#range prints from n2 to 0 where -1 is the step.
for n2 in range (n2, 0, -1):
    print ("*" * n2)
