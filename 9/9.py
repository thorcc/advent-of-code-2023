import re

file = open("input.txt")
data = file.read()
lines = data.split("\n")

nums = []

for line in lines:
    nums.append(list(map(int, line.split(" "))))

def add(vals):
    new_vals = []
    for i in range(0, len(vals) - 1):
        new_vals.append(vals[i + 1] - vals[i])
    return new_vals

def get_val_lists(vals, lists=[]):
    new_list = lists.copy()
    new_list.append(vals)
    if sum(map(abs, vals)) == 0:
        return lists
    return get_val_lists(add(vals), new_list)

lists = []
for num in nums:
    lists.append(get_val_lists(num))

# a
sum_difs = 0
for list_ in lists:
    diff = 0
    for i in range(len(list_) - 1, -1, -1):
        diff = diff + list_[i][-1]
    sum_difs += diff

print(sum_difs)

# b
sum_difs = 0
for list_ in lists:
    diff = 0
    for i in range(len(list_) - 1, -1, -1):
        diff = list_[i][0] - diff
    sum_difs += diff

print(sum_difs)