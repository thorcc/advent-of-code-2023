file = open("input.txt")
data = file.read()
sequence = data.split(",")

total = 0

for s in sequence:
    s_total = 0
    for c in s:
        s_total = ((s_total + ord(c)) * 17) % 256
    total += s_total

print(total)
