import re
rawdata = []

with open("input.txt") as f:
    rawdata = f.readlines()
rawdata = [n.strip() for n in rawdata]
data = {}

for line in rawdata:
    newline = line.split(" contain ")
    newline = [re.sub(" *bags* *", "", n).strip(".") for n in newline]
    # Make this a dictionary
    data[newline[0]] = [n.strip() for n in newline[1].split(",")]

# At this point data is a dictionary of bag colours(key) and lists of contents (value) 
# in the format 'n colour' e.g. 5 vibrant indigo

# Can a given list of bags contain a shiny gold bag?
def count_bags_inside(dict_of_bags, bag_color):

    print("CHECKING " + bag_color)
    print(bag_color + " contains: " + str(dict_of_bags[bag_color]))
    
    # Get rid of the numbers (in a nasty way)
    number_index = [re.search("^[0-9]+ ", n) for n in dict_of_bags[bag_color]]
    if None in number_index:
        # There were no numbers in the list, therefore no new bags contained here
        print("No more")
        return 0
    else:
        # Isolate the bag type and the bag number in separate lists
        list_of_bags = [n.strip("0123456789 ") for n in dict_of_bags[bag_color]]
        list_of_numbers = [int(n[:number_index[ind].end()]) for ind, n in enumerate(dict_of_bags[bag_color])]
        
        results = []
        
        # Loop through the list of bags contained within this one
        for i in range(len(list_of_bags)):

            # Count how many bags are inside each of these bags
            check_bag = count_bags_inside(dict_of_bags, list_of_bags[i])

            # Save the results as a list
            print("Saving " + str(check_bag))
            results.append(check_bag)
        
        # What did I find?
        print("Inside this bag I found " + str(results))
        total = 0
        for result in results:
            total += result
        print("Returning ", total)
        return total


print("Total bags inside - ", count_bags_inside(data, "plaid plum"))

# 1470 too high