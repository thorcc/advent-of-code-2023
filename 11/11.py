file = open("input.txt")
data = file.read()
lines = data.split("\n")
universe = [list(line) for line in lines]

def expand(list_, n, ex):
    c = 0
    for num in list_:
        if n > num:
            c += 1
    return ex * c

empty_rows = []
empty_cols = []

for i in range(len(universe)):
    if "#" not in universe[i]:
        empty_rows.append(i)

for i in range(len(universe[0])):
    empty = True
    for j in range(len(universe)):
        if universe[j][i] == "#":
            empty = False
            break
    if empty:
        empty_cols.append(i)
        

# a

galaxies = set()

for i in range(len(universe)):
    for j in range(len(universe[i])):
        if universe[i][j] == "#":
            x = i + expand(empty_rows, i, 1)
            y = j + expand(empty_cols, j, 1)
            galaxies.add((x, y))

lengths = {}

for galaxy in galaxies:
    for other_galaxy in galaxies:
        if other_galaxy != galaxy and ((other_galaxy, galaxy)) not in lengths:
            lengths[(galaxy, other_galaxy)] = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])


sum = 0
for l in lengths.values():
    sum += l
print(sum)


# b

for i in range(len(universe)):
    for j in range(len(universe[i])):
        if universe[i][j] == "#":
            x = i + expand(empty_rows, i, 999_999)
            y = j + expand(empty_cols, j, 999_999)
            galaxies.add((x, y))
lengths = {}

for galaxy in galaxies:
    for other_galaxy in galaxies:
        if other_galaxy != galaxy and ((other_galaxy, galaxy)) not in lengths:
            lengths[(galaxy, other_galaxy)] = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])

sum = 0
for l in lengths.values():
    sum += l
print(sum)
