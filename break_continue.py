#!/usr/bin/env python

'''
The break statement in Python terminates the current loop and resumes execution at the next statement, just like the traditional break found in C.
The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in
both while and for loops.
'''
for n in range (2,10):
    for x in range (2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        print n, 'is a prime number'

'''
The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements
in the current iteration of the loop and moves the control back to the top of the loop. The continue statement can be used in both while and for loops.
'''
for num in range (2,10):
    if num % 2 == 0:
        print 'Found an even number', num
        continue
    print 'Found an odd number', num
