#Write a program to print 'Hello World'

#!/usr/bin/env python
print ("Hello World")

#Write a program to take two number as inputs and perform arithmetic operations on them.

a = input("Enter the first number")
b = input("Enter another number")

sum = int(a) + int(b)
print ("The sum of given numbers is", sum)

diff = int(a) - int(b)
#This if block will determine if the first number you entered is smaller and show the difference as a natural number.
if diff < 0:
    diff = int(b) - int(a)
    print ("The difference between the given numbers is", diff)
else:
    print ("The difference between the numbers is", diff)

mult = int(a) * int(b)
print ("The product of the given mumbers is", mult)
