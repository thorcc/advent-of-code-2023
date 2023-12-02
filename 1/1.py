# file = open("example.txt")
file = open("input.txt")
data = file.read()
lines = data.split("\n")
total = 0
for line in lines:
    line_vals = []
    for char in line:
        if char.isnumeric():
            line_vals.append(int(char))
    total += int( str(line_vals[0]) + str(line_vals[-1]))
print(total)

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

total = 0
for line in lines:
    line_vals = []
    for i in range(len(line)):
        if line[i].isnumeric():
            line_vals.append(int(line[i]))
        else:
            for j in range(6):
                word = line[i:i+j]
                if word in numbers:
                    line_vals.append(numbers[word])
                    break
    total += int(str(line_vals[0]) + str(line_vals[-1]))
print(total)