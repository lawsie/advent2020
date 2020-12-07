import re
rawdata = []

with open("input.txt") as f:
    rawdata = f.readlines()

rawdata = [n.strip() for n in rawdata]


data = []

for line in rawdata:
    newline = line.split(" contain ")
    newline = [re.sub(" *bags* *", "", n).strip(".") for n in newline]
    # Make this a diction ary
    data.append(newline)

[print(n) for n in data]
