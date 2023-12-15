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

# ---- TULL! --------

# def turn_left(vector):
#       x,y = vector
#       return (-y,x)

# def turn_right(vector):
#     return turn_left(turn_left(turn_left(vector)))

# outside = set()
# inside = set()

# direction = (loop[0][0] - loop[-1][0], loop[0][1] - loop[-1][1])
# # in_dir = turn_right(direction)
# in_dir = turn_left(direction)

# print(direction)
# # print(out_dir)
# print(in_dir)

# dirs = {
#      (-1,  0): "👆",
#      ( 1,  0): "👇",
#      ( 0, -1): "👈", 
#      ( 0,  1): "👉"
# }

# for i in range(len(loop) - 1):
#     x, y = loop[i]
#     symbol = lines[x][y]
#     print(f"({x},{y}): '{symbol}' dir: {dirs[direction]} in_dir: {dirs[in_dir]}")
#     if symbol not in ["-", "|"]:
#         direction = (loop[i + 1][0] - loop[i][0], loop[i + 1][1] - loop[i][1])
#         # in_dir = turn_right(direction)
#         in_dir = turn_left(direction)
#         # print(f"i: {i} - Symbol: {symbol} - ({x},{y}): {direction}, in_dir: {in_dir}")
#     else:
#         x += in_dir[0]
#         y += in_dir[1]
#         while (x,y) not in loop and (x,y) not in inside:
#             inside.add((x,y))
#             print((x,y))
#             x += in_dir[0]
#             y += in_dir[1]
# print(inside)
            
# ------
            
# Tips på reddit: 
#    - https://en.wikipedia.org/wiki/Pick%27s_theorem
#    - https://en.wikipedia.org/wiki/Shoelace_formula
            
def area_shoe(points):
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area_2 = 0
    for i in range(len(points) - 1):
        x = points[i]
        y = points[i + 1]
        area_2 += x[0] * y[1] - x[1] * y[0]
    x = points[-1]
    y = points[0]
    area_2 += x[0] * y[1] - x[1] * y[0]
    return area_2 / 2

area = area_shoe(loop)


# https://en.wikipedia.org/wiki/Pick%27s_theorem
i = area - (len(loop) / 2) + 1
print(i)