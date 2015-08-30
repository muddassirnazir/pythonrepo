#Author: Muddassir Nazir

#Strings and Loops
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
DaysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for cntr in range(0,12):    print '%s has %d days' %(month[cntr],DaysOfMonth[cntr])
