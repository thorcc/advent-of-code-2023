# from collection import defaultdict
file = open("example.txt")
data = file.read()
lines = data.split("\n")


# Lager en graf med noder (edges) og kanter (vertices)

edges = {}
vertices = set()

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            start = (i, j)
        if lines[i][j] != ".":
            edges[(i,j)] = lines[i][j]

def find_neighbors(edge):
    x, y = edge
    symbol = lines[x][y]
    neighbors = []
    if symbol in ["-", "7", "S", "J"]:
        if (x, y - 1) in edges:
            if edges[(x, y - 1)] in ["-", "L", "F"]:
                neighbors.append((x, y - 1))
    if symbol in ["-", "L", "F", "S"]:
        if (x, y + 1) in edges:
            if edges[(x, y + 1)] in ["-", "J", "7"]:
                neighbors.append((x, y + 1))
    if symbol in ["|", "J", "L", "S"]:
        if (x - 1, y) in edges:
            if edges[(x - 1, y)] in ["|", "7", "F"]:
                neighbors.append((x -1, y))
    if symbol in ["|", "7", "F", "S"]:
        if (x + 1, y) in edges:
            if edges[(x + 1, y)] in ["|", "L", "J"]:
                neighbors.append((x + 1, y))
    return neighbors
 
visited = {}
visited[start] = 0
queue = [start]
i = 1
while len(queue) > 0:
    current = queue.pop(0)
    neighbors = find_neighbors(current)
    for n in neighbors:
        if n not in visited:
            visited[n] = visited[current] + 1
            queue.append(n)

distances = list(visited.values())
distances.sort()
# print(distances[-1])

visited = {}
visited[start] = [start]
queue = [start]

while len(queue) > 0:
    current = queue.pop(0)
    neighbors = find_neighbors(current)
    for n in neighbors:
        if n not in visited:
            visited[n] = visited[current] + [n]
            queue.append(n)


loop = list(visited.values())[-1] + list(visited.values())[-2]

size_x = len(lines)
size_y = len(lines[0])

def find_not_loop_ns(current):
    x, y = current
    neighbors = []
    if x > 0 and (x - 1, y) not in loop:
        neighbors.append((x - 1, y))

    if x < size_x - 1 and (x + 1, y) not in loop:
        neighbors.append((x + 1, y))

    if y > 0 and (x, y - 1) not in loop:
        neighbors.append((x, y - 1))

    if y < size_y - 1 and (x, y + 1) not in loop:
        neighbors.append((x, y + 1))

    return neighbors

outside = set()

def find_cluster(start):
    visited = set()
    visited.add(start)
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        neighbors = find_not_loop_ns(current)
        for n in neighbors:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return visited


for i in range(size_x):
    j = 0
    if (i,j) not in loop and (i,j) not in outside:
        v = find_cluster((i, j))
        outside = outside.union(v)
    j = size_y - 1
    if (i,j) not in loop and (i,j) not in outside:
        v = find_cluster((i, j))
        outside = outside.union(v)
for j in range(size_y):
    i = 0
    if (i,j) not in loop and (i,j) not in outside:
        v = find_cluster((i, j))
        outside = outside.union(v)
    i = size_x - 1
    if (i,j) not in loop and (i,j) not in outside:
        v = find_cluster((i, j))
        outside = outside.union(v)

all = set(loop).union(outside)
inside = set()
for i in range(size_x):
    for j in range(size_y):
        if (i, j) not in all:
            inside.add((i,j))

loop = [(x[1], x[0]) for x in loop]
outside = [(x[1], x[0]) for x in outside]
inside = [(x[1], x[0]) for x in inside]

import matplotlib.pyplot as plt
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, sharex=True)
ax1.scatter(*zip(*loop), c=["blue"])
ax1.scatter(*zip(*outside), c=["red"])
ax1.scatter(*zip(*inside), c=["orange"])
ax1.set_title(f'Outside ({len(outside)}), loop ({len(loop)}) and inside ({len(inside)})')
plt.show()
