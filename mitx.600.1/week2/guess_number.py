#In this problem, you'll create a program that guesses your secret number!
print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = False

while not guess:
    ans = (high + low)/2
    print("Is your secret number " + str(ans) + "? ")

    my_num = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. \
    Enter 'c' to indicate I guessed correctly.")

    if my_num == 'h':
        high = ans

    elif my_num == 'l':
        low = ans

    elif my_num == 'c':
        print("Game over. Your secret number was: " + str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")
