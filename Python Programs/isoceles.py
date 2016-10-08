#!/usr/bin/python3
#Enter the side lenghts first
#Logic : Two of the three sides are equal
#Equilateral triangle is also be a isoceles
print ("First we have to enter sides of the triangle")
a = int (input("Enter the length of side a"))
b = int(input("Enter the length of side b"))
c = int(input("Enter the length of side c"))

#Write a program to check sides of a triangle and tell what type of triangle it is.
if a == b or b == c or c == a:
    print ("The triangle is isoceles")
else:
    print ("Not Isoceles")

#Write a program to check if a triangle is right angled
#Logic : The square of sum of two sides is greater than the square of third side.
if ((a + b) ** 2) > (c ** 2) or ((b + c) ** 2) > (a ** 2) or ((c + a) ** 2) > (b ** 2):
    print ("We have a right angled triangle")
else:
    print ("Not right angled")
