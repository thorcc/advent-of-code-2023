import re
file = open("input.txt")
data = file.read()
lines = data.split("\n")

times = list(map(int, re.findall(r'\d+', lines[0])))
records = list(map(int, re.findall(r'\d+', lines[1])))
possibilities = []

for i in range(len(times)):
    time = times[i]
    record = records[i]
    n = 0
    for j in range(time):
        length = j * (time - j)
        if length > record:
            n += 1
    possibilities.append(n)
print(possibilities)

sum = 1
for p in possibilities:
    sum *= p
print(sum)


time = int(''.join([str(x) for x in times]))
record = int(''.join([str(x) for x in records]))

n = 0
for j in range(time):
    length = j * (time - j)
    if length > record:
        n += 1
    if j % 10_000_000 == 0:
        print(f"{j}/{time}")
print(n)

