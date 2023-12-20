import numpy as np

file = open("input.txt")
data = file.read()
lines = data.split("\n")

patterns = []
i = 0

pattern = []
for line in lines:
    if line == '':
        patterns.append(np.array(pattern))
        i += 1
        pattern = []
    else:
        pattern.append(list(line))


# a
def check(pattern, left, right):
    while np.array_equal(pattern[left], pattern[right]):
        if left == 0 or right == len(pattern) -1:
            return i + 1
        left -= 1
        right += 1
    return -1

sum = 0

for pattern in patterns:
    for i in range(len(pattern) - 1):
        if np.array_equal(pattern[i], pattern[i + 1]):
            above = check(pattern, i, i + 1)
            if above != -1:
                sum += 100 * above
                break

    pattern_T = pattern.T
    for i in range(len(pattern_T) - 1):
        if np.array_equal(pattern_T[i], pattern_T[i + 1]):
            left = check(pattern_T, i, i + 1)
            if left != -1:
                sum += left
                break
        
print(sum)

# b
        
def check(pattern, start):
    err = 0
    over = start
    under = start + 1
    while err <= 1: # or np.array_equal(pattern[left], pattern[right]):
        if over < 0 or under > len(pattern) -1:
            break
        for i in range(len(pattern[over])):
            if pattern[over][i] != pattern[under][i]:
                err += 1
        over -= 1
        under += 1
    if err == 1:
        return start + 1
    return -1

sum = 0
p = 0
for pattern in patterns:
    found = False
    for i in range(len(pattern) - 1):
        above = check(pattern, i)
        if above != -1:
            sum += 100 * above

    pattern_T = pattern.T
    for i in range(len(pattern_T) - 1):
        left = check(pattern_T, i)
        if left != -1:
            sum += left
    p += 1

print(sum)            