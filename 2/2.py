# file = open("example.txt")
#file = open("/Users/tcc/Kode/advent-of-code/2023/2/example.txt")
file = open("input.txt")
data = file.read()
lines = data.split("\n")
max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}
possible_games = []
for line in lines:
    possible = True
    first, second = line.split(":")
    game_id = int(first.split(" ")[1])
    hands = second.strip().split(";")
    for hand in hands:
        cubes = hand.strip().split(",")
        for cube in cubes:
            n, c = cube.strip().split(" ")
            if int(n) > max_cubes[c]:
                possible = False
    if possible: 
        possible_games.append(game_id)

print(sum(possible_games))

powers = 0
for line in lines:
    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    _, second = line.split(":")
    hands = second.strip().split(";")
    for hand in hands:
        cubes = hand.strip().split(",")
        for cube in cubes:
            n, c = cube.strip().split(" ")
            if int(n) > max_cubes[c]:
                max_cubes[c] = int(n)
    power = 1
    for val in max_cubes.values():
        power *= val
    powers += power

print(powers)

