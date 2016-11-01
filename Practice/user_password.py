#Program to check username and passwords
#Use of simple if, else, strings and raw_input
#Author: Muddassir Nazir

username = ['John', 'Alice', 'Bob', 'Mary']
password = ['qwert', 'zcxcv', 'asdf', '1234']

user = raw_input('Enter the username')
passwd = raw_input('Enter your password')

#Check if user is in the list
if user in username:
    position = username.index(user) #Get the position of user in the list of users
    if passwd == password[position]: #Find the password at position
        print 'Hi there, %s. Access granted.' %user
    else:
        print "Password incorrect. Access denied."
else:
     print "Sorry..User doesn't existent. Access denied."
