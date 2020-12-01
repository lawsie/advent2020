with open("input.txt") as f:
    data = f.readlines()
    current = 0
    for item in data:
        for current in range(len(data)):
            if int(item) + int(data[current]) == 2020:
                print("Found - " + item + data[current])
                print("Product is " + str(int(item) * int(data[current])) )
