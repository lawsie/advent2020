ok_bags = ["shiny gold"]

# Repeat this process until no new ok bags are found
while True:
    new_bags = []
    for bag_color, contents in data.items():
        #print(bag_color.upper(), end=": ")
        for each in contents:
            # Find the position of the number at the start so you can get rid of it
            number = re.search("^[0-9]+ ", each)
            if number is not None:
                inner_bag = each[number.end():]  # Just get the text from the list
                if inner_bag in ok_bags and bag_color not in ok_bags:
                    new_bags.append(bag_color)
                    #print("Found " + inner_bag, end=" ")
        #print("\n")
    print("New bags found this iteration: " + str(new_bags))
    if len(new_bags) > 0:
        print("Please continue")
        new_bags = []
    else:
        break    

