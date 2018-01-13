#Cube root approximation using bisection search
cube = 27
ep = 0.01
guess = 0
low = 1
high = cube
ans = (high+low)/2.0

while abs(ans**3 - cube) >= ep:
    if ans**3 < cube:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
    guess = guess + 1
print('Number of guesses = ', guess)
print(str(ans), 'is close to cube root of ' + str(cube))
