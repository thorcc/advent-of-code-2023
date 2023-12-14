import re
import math
file = open("input.txt")
data = file.read()
lines = data.split("\n")

instructions = lines[0]
print(instructions)


def check(p):
    if p[-1] != "Z":
        return False
    return True

network = {}
pos = []
counts = []

for line in lines[2:]:
    key, l, r = re.findall(r'[A-Z0-9]+', line)
    network[key] = {"L": l, "R": r}
    if key[-1] == "A":
        pos.append(key)


i = -1
for p in pos:
    count = 0
    while not check(p):
        i += 1
        if i >= len(instructions):
            i = 0
        p = network[p][instructions[i]]
        count += 1
    counts.append(count)

# Finner minste felles multiplum (least common multiplier)
print(math.lcm(*counts))
