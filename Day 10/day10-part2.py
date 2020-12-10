with open("input.txt") as f:
    data = f.readlines()

data = [int(n.strip()) for n in data]
data.sort()

# You now have a sorted list of integers
device_jolts = 170
last_jolts = 0

differences = []

for adapter in data:
    # Calculate the difference between this adapter and the last one
    diff = adapter - last_jolts
    differences.append(diff)
    last_jolts = adapter

# Don't forget the device
differences.append(device_jolts-data[len(data)-1])

result = differences.count(1) * differences.count(3)

print(result)