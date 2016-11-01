#!/usr/bin/python3.5
#Program to print fibonacci series : The next number is sum of previous two numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

print ("Printing fibonacci series")
nterm = int(input("Enter the number of terms"))
a, b = 0, 1

for i in range(nterm):
    print (a)
    a, b = b, a + b
