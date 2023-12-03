# file = open("example.txt")
file = open("input.txt")
data = file.read()
lines = data.split("\n")

numbers = {}

for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
        num = ""
        k = j
        char = lines[i][k]
        if lines[i][k].isnumeric():
            while k < len(lines[i]) and lines[i][k].isnumeric():
                num += lines[i][k]
                k += 1
            coords = []
            for l in range(j,k):
                coords.append((i,l))
            for l in range(j,k):
                numbers[(i,l)] = {
                    "num": int(num),
                    "others": coords
                }
            j = k
        else:
            j += 1

total = 0
counted = []

def check(i,j):
    global total, counted
    if (i,j) not in counted and (i,j) in numbers:
        total += numbers[(i,j)]["num"]
        counted = counted + numbers[(i,j)]["others"]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if not (char == "." or char.isnumeric()):
            for k in range(-1, 2):
                for l in range(-1,2):
                    check(i+k, j+l)

print(total)

counted = []

def check(i,j):
    global counted
    if (i,j) not in counted and (i,j) in numbers:
        counted = counted + numbers[(i,j)]["others"]
        return numbers[(i,j)]["num"]
    return 0

total = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        char = lines[i][j]
        if char == "*":
            adjacents = 0
            gear_ratio = 1
            for k in range(-1, 2):
                for l in range(-1,2):
                    num = check(i+k,j+l)
                    if num > 0:
                        adjacents += 1
                        gear_ratio *= num
            if adjacents > 1:
                total += gear_ratio
print(total)
