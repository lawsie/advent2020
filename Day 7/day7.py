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
def check_bag(dict_of_bags, bag_color):
    
    # Get rid of the numbers (in a nasty way)
    list_of_bags = [n.strip("0123456789 ") for n in dict_of_bags[bag_color]]
    print(list_of_bags)

    # Base cases
    if "no other" in list_of_bags:
        return False
    elif "shiny gold" in list_of_bags:
        return True
    else:
        results = []
        for bag in list_of_bags:
            results.append(check_bag(dict_of_bags, bag))
        
        if True in results:
            return True
        else:
            return False
    
good_bags = 0

for key in data:
    if check_bag(data, key):
        good_bags += 1

print("Good bags - " + str(good_bags))