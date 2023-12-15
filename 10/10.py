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
print(distances[-1])

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
loop.sort()
# print(loop)

size_x = len(lines)
size_y = len(lines[0])

def check_up(i, j):
    k = i
    while k > -1:
        if (k,j) in loop:
            return True
        k -= 1
    return False

def check_down(i, j):
    k = i
    while k < size_x:
        if (k,j) in loop:
            return True
        k += 1
    return False

def check_left(i, j):
    k = j
    while k > -1:
        if (i,k) in loop:
            return True
        k -= 1
    return False

def check_right(i, j):
    k = j
    while k < size_y:
        if (i,k) in loop:
            return True
        k += 1
    return False


def check_inside(i, j):
    return check_up(i, j) and check_down(i, j) and check_left(i, j) and check_right(i, j)

inside = []
for i in range(size_x):
    for j in range(size_y):
        if (i,j) not in loop:
            if check_inside(i,j):
                inside.append((i,j))
print(inside)



import matplotlib.pyplot as plt
plt.scatter(*zip(*loop))
# plt.show()
plt.scatter(*zip(*inside))
plt.show()


# visited = {}

# def dfs(current, i):
#     visited[current] = i
#     neighbors = find_neighbors(current)
#     for n in neighbors:
#         if n not in visited or visited[n] > i:
#             dfs(n, i + 1)

# dfs(start, 0)
# distances = list(visited.values())
# distances.sort()
# print(distances[-1])