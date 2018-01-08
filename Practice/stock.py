#!/usr/bin/env python

# Compute the value of a block of stock

shares = int( raw_input("shares: ") )
price = float( raw_input("dollars: ") )
price += float( raw_input("eights: ") )/8.0
print ("value", shares * price)
