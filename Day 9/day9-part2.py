import copy

with open("input.txt") as f:
    data = f.readlines()
    data = [int(n.strip()) for n in data]

# Define the search area
start = 0
end = 25
target = 104054607  # The number from part 1

# First get rid of any numbers that are bigger than the target
smaller_data = [n for n in data if n < target]

# Reverse the list to look at the bigger numbers first
smaller_data.reverse()

for i in range(len(smaller_data)):

    data_for_loop = copy.deepcopy(smaller_data)
    
    # Look at each number and add it together with the remaining list
    current = data_for_loop[i]
    end = len(data_for_loop)
    rest = data_for_loop[i+1:end]

    found_it = False

    while end > i+1:
        #print("Trying ", str(rest))

        if sum(rest) == target:
            found_it = True
            rest.sort()
            print("I made ", target, " using ", str(rest))
            print("The sum of the start and end was " + str(rest[0] + rest[len(rest)-1]))
            break
        else:
            end = end - 1
            rest = data_for_loop[i+1:end]
        
    if not found_it:
        print("Didn't find it for i ", i)
    else:
        break
    

# 11828200 too low