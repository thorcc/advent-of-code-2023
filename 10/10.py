# from collection import defaultdict
file = open("input.txt")
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

current = start
neighbors = find_neighbors(current)
distances = list(visited.values())
distances.sort()
print(distances[-1])