#!/usr/bib/env python

# Convert 8 C to F
C=37.5
F=32+C*(9./5.)
print "celsius",C,"fahrenheit",F

#Fibonacci Series
a, b = 0, 1
while b < 20:
    print b
    a, b = b, a + b

# Compute line between two points.
x1,y1 = 2,3 # point one
x2,y2 = 6,8 # point two
m,b = float(y1-y2)/(x1-x2), y1-float(y1-y2)/(x1-x2)*x1
print "y=",m,"*x+",b
