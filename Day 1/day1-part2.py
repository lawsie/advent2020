import itertools

with open("input.txt") as f:
    data = f.readlines()
    potentials = list(itertools.combinations(data,3))
    for tup in potentials:
        tup = [int(n.strip()) for n in tup]
        if  tup[0] + tup[1] + tup[2] == 2020:
            print("Found it!")
            print(tup)
            print(tup[0]*tup[1]*tup[2])
