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
    for response in group:
        this_group += response
    
    this_group = set([char for char in this_group])
    
    total_yeses += len(this_group)


print(total_yeses)
    


