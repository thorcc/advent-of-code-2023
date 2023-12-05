file = open("input.txt")
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
all_seeds = []
for i in range(len(maps) + 1):
    all_seeds.append([])
all_seeds[0] = [(seeds[i],seeds[i + 1]) for i in range(0,len(seeds)-1, 2)]

for i in range(len(maps)):
    while len(all_seeds[i]) > 0:
        seed = all_seeds[i][0]

        
        for j in range(len(maps[i])):
            seed_start = seed[0]
            seed_end = seed[0] + seed[1]
            map = maps[i][j]
            map_start = map[1]
            map_end = map[1] + map[2]
            if seed_start >= map_start and seed_end <= map_end:
                # hele intervallet er innafor
                all_seeds[i + 1].append((seed[0] + map[0] - map[1], seed[1]))
                all_seeds[i].pop(0)
                break
            elif seed_end <= map_start or seed_start >= map_end:
                # hele intervallet er utenfor
                # all_seeds[i + 1].append(seed)
                # all_seeds[i].pop(0)
                pass
            elif seed_start < map_start:
                # deler av intervallet er under
                all_seeds[i].append((map_start, seed_end - map_start))
                all_seeds[i].append((seed_start, map_start - seed_start))
                all_seeds[i].pop(0)
                break
            elif seed_end > map_end:
                # deler av intervallet er over
                all_seeds[i].append((map_end, seed_end - map_end))
                all_seeds[i].append((seed_start, map_end - seed_start))
                all_seeds[i].pop(0)
                break
        if (j == len(maps[i]) - 1) and seed in all_seeds[i]:
            all_seeds[i+1].append(seed)
            all_seeds[i].pop(0)

siste = all_seeds[-1]
print(sorted(siste)[0])
            # deler av intervallet er innafor