s = "bobobdgrtghrgfgg"
counter = 0
for char in range(len(s) - 2):
    if s[char] == 'b' and s[char + 1] == 'o' and s[char + 2] == 'b':
        counter += 1

print ('Number of times bob occurs is:', counter)
