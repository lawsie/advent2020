data = []
total_yeses = 0

with open("input.txt") as f:
    # Use the same input from day 4
    current_record = []

    for line in f:

        if line != "\n":
            current_record = current_record + line.split(" ")

        else:
            current_record = [n.strip() for n in current_record]
            data.append(current_record)
            current_record = []
    
    # Don't forget the last one!! Doh
    current_record = [n.strip() for n in current_record]
    data.append(current_record)


# So now we have a list (data) of lists. Each list is one group of passengers' responses

for group in data:
    this_group = ""
    num_in_group = len(group)
    #print(group)
    #print("There are " + str(num_in_group) + " in this group")

    # Find the longest string in the group
    longest = max(group, key=len)

    group_yeses = 0
    
    # Loop through the longest string to check whether each letter is also in the other strings
    for letter in longest:
        letter_ok = True
        for response in group:
            if letter not in response:
                letter_ok = False
        # If the letter is OK by now, count it as a yes
        if letter_ok:
            group_yeses += 1
    
    total_yeses += group_yeses
    


print(total_yeses)
    


