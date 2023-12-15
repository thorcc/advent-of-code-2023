import math
file = open("input.txt")
data = file.read()
lines = data.split("\n")

edges = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            start = (i, j)
        if lines[i][j] != ".":
            edges[(i,j)] = lines[i][j]

loop = []
i = 0
current = (-1,-1)
prev = (-1,-1)
while current != start:
    if i == 0:
        current = start
    i += 1
    x, y = current
    symbol = edges[current]
    if (x, y - 1) != prev and symbol in ["-", "7", "S", "J"] and (x, y - 1) in edges and edges[(x, y - 1)] in ["-", "L", "F", "S"]:
            prev = current
            current = (x, y - 1)
            loop.append(current)
    elif (x, y + 1) != prev and symbol in ["-", "L", "F", "S"] and (x, y + 1) in edges and edges[(x, y + 1)] in ["-", "J", "7", "S"]:
            prev = current
            current = (x, y + 1)
            loop.append(current)
    elif (x - 1, y) != prev and symbol in ["|", "J", "L", "S"] and (x - 1, y) in edges and edges[(x - 1, y)] in ["|", "7", "F", "S"]:
            prev = current
            current = (x - 1, y)
            loop.append(current)
                
    elif (x + 1, y) != prev and symbol in ["|", "7", "F", "S"] and (x + 1, y) in edges and edges[(x + 1, y)] in ["|", "L", "J", "S"]:
            prev = current
            current = (x + 1, y)
            loop.append(current)

print(loop)
print(math.ceil(len(loop) / 2))

