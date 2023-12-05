file = open("example.txt")
data = file.read()
lines = data.split("\n")

seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
maps = []

line_n = 1
i = -1
while line_n < len(lines):
    if lines[line_n] == "":
        maps.append([])
        line_n += 2
        i += 1
    else:
        nums = [int(x) for x in lines[line_n].split(" ")]
        maps[i].append(nums)
        line_n += 1 

# for i in range(len(seeds)):
#     seed = seeds[i]
#     for scenario in maps:
#         for map in scenario:
#             if seed >= map[1] and seed < map[1] + map[2]:
#                 seed = seed + (map[0] - map[1])
#                 break
#     seeds[i] = seed
# seeds.sort()
# print(seeds[0])


#b
all_seeds = [[]]*(len(maps) + 1)
all_seeds[0] = [(seeds[i],seeds[i + 1]) for i in range(len(seeds)-1)]

for i in range(len(maps)):
    print(maps[i])
    for seed in all_seeds[i]:
        for map in maps[i]:
            if seed[0] >= map[1] and (seed[0] + seed[1]) < map [1] + map[2]:
                # hele intervallet er innafor
                all_seeds[i + 1].append((seed[0] + map[0] - map[1], seed[1]))
                break
            if seed[0] + seed[1] <= map[1] or seed[0] >= map[1] + map[2]:
                # hele intervallet er utenfor
                all_seeds[i+1].append(seed)
                print(all_seeds)
                # neste.append(seed)
                break
            
            # deler av intervallet er innafor