with open("input.txt") as f:
    data = f.readlines()
    data = [int(n.strip()) for n in data]

# Define the search area
start = 0
end = 25
current = 25    # The number we're looking at

# Check whether the current number can be made up of any of the previous numbers added together
def check_number(start, end, current, data):
    search_list = data[start:end]
    find = data[current]
    for first in search_list:
        for ind, second in enumerate(search_list):
            if first + second == find:
                return True
    return False



while current < len(data):
    if check_number(start, end, current, data):    
        current += 1
        start += 1
        end += 1
    else:
        print("Number ", data[current], " has no sums")
        break

