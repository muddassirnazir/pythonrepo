#Using builtin math functions
import math

#Raise x to power y
print pow(4,3)
#Print a number as a float value
print float(23)
#Print a complex number with 3 as real and 2 as imaginary parts
print complex(3,2)
#COnvert a number to binary
print bin(245)
print math.pi

sum, count = 0, 0
average = float(sum)/count
average = count != 0 and sum/count
print average

import random

print random.choice(['red', 'blue', 'green'])

# Simple Range 0 <= r < 6
print random.randrange(6), random.randrange(6)
# More complex range 1 <= r < 7
print random.randrange(1,7), random.randrange(1,7)
# Really complex range of even numbers between 2 and 36
print random.randrange(2,37,2)
# Odd numbers from 1 to 35
print random.randrange(1,36,2)
