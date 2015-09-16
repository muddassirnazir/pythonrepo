#Using random module

import random
for x in range(0,10):
    print random.randint(0,55)

#Specifically using the randint function from the random module
from random import randint
for cntr in range(0,14):
    print randint(1,99)

#Defining a function
def my_function():
    print "Hello...I have defined a function and I am gonna call it my_function and I am gonna call it to print this sentence"
    print "We can use functions to reduce the repetitive tasks"
    print "functions reduce the chances of error as we are making our code readable and clutter free"

my_function()

def TopOrBottom(width):
# width is total width of returned line
    return '%s%s%s' %('+',('=' * (width-2)),'+')

print TopOrBottom(40)
