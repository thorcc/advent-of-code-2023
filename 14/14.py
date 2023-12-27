import numpy as np
file = open("input.txt")
lines = file.read().split("\n")

platform = np.full((len(lines[:-1]), len(lines[0])), '', dtype="str")

for i in range(len(lines[:-1])):
   for j in range(len(lines[i])):
      platform[i][j] = lines[i][j]


def tilt(p):
   for line in p:
      for i in range(len(line)):
         if line[i] == "O":
            line[i] = "."
            j = i
            while j > 0 and line[j - 1] == ".":
               j -= 1
            line[j] = "O"
   return p

def cycle(p):
   p = tilt(p.T) # north
   p = tilt(p.T) # west
   p = tilt(np.flip(p, axis=0).T) # south
   p = tilt(np.flip(p, axis=0).T) # east
   p = np.flip(p)
   return p


visited = {}
i = 0
cycles = 1_000_000_000
found = 0

while i < cycles:
   i += 1
   platform = cycle(platform)
   flat = "".join(platform.flatten())
   total = 0

   if flat in visited and not found:
      print(f"i: {i}, found: {visited[flat]}, total: {total}")
      found = visited[flat]
      print(cycles % (i - found))
      cycles = i + ((cycles - i) % (i - found))
   else:
      visited[flat] = i



total = 0

for line in platform.T:
   for i in range(len(line)):
      if line[i] == "O":
         total += len(line) - i

print(total)
