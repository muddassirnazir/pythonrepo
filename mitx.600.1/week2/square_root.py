#Square root approximation using bisection search
x = 25
ep = 0.01
guess = 0
low = 0.0
high = x
ans = (high+low)/2.0

while abs(ans**2 -x) >= ep:
    print('low = ' + str(low) + 'high = ' + str(high))
    guess = guess + 1
    if ans**2 <x:
        low = ans

    else:
        high = ans
    ans = (high + low)/2.0
print('guess  = ' + str(guess))
print(str(ans) + ' is close to square root of ' + str(x))
