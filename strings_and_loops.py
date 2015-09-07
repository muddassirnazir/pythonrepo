#Author: Muddassir Nazir

#Strings and Loops
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
DaysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for cntr in range(0,12):    print '%s has %d days' %(month[cntr],DaysOfMonth[cntr])

st = 'He said, "Don\'t worry"'

#While loops

x = 3

while x != 0:
	print(x)
	x = x - 1
	print("Wow, we've counted x down, and now it equals", x)
	print "And now the loop has ended."

if x == 10:
	print "x is 10"
elif x < 5:
	print "x is less than 5"
else:
	print "x is something else"

print 'Hello'
print 'Muddassir\'s phone'
print "He said, \"Don\'t worry\""

count = 10
while count >= 1:
	count = count - 1
	print count

loop = 1
while loop == 1:
	response = raw_input("Write something or type 'quit' to exit =>")
	if response == 'quit':
		print "Quitting now"
		loop = 0
	else:
		print 'You typed %s'	% response

string = "This is a string and I am gonna split it"
print string.split(' ')
