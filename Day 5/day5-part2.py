with open("input.txt") as f:

    data = f.readlines()
    data = [n.strip() for n in data]

seat_ids = []

for seat in data:
    # Chop the data up into the data for rows and data for columns
    row = seat[:-3]
    col = seat[-3:]

    # Sort out the rows first with a binary search
    # Rows are 0 through 127 (so 128 total)
    row_low = 0
    row_high = 127

    # Loop through all the row data narrowing the range
    for pos in row:
        mid = row_low + ((row_high - row_low) // 2)   # Round down
        if pos == "F":
            # Front means the lower half
            row_high = mid
        elif pos == "B":
            # Back means the upper half
            row_low = mid + 1
    
        #print("Low: " + str(row_low) + " High: " + str(row_high))

    # So now we know (as either low/high var) which row

    # Cols are 0 through 7
    col_low = 0
    col_high = 7

    # Loop through all the row data narrowing the range
    for pos in col:
        mid = col_low + ((col_high - col_low) // 2)   # Round down
        if pos == "L":
            # Front means the lower half
            col_high = mid
        elif pos == "R":
            # Back means the upper half
            col_low = mid + 1
    
        #print("Low: " + str(col_low) + " High: " + str(col_high))
    
    # Calculate seat ID
    seat_id = (row_low * 8) + col_low
    seat_ids.append(seat_id)
    
# Sort seat ids
seat_ids.sort()

# Look through each element and check whether there are elements either side
for index, seat_id in enumerate(seat_ids):
    if index == 0 or index == len(seat_ids)-1:
        pass
    else:
        if seat_ids[index-1] == seat_id-1 and seat_ids[index+1] == seat_id+1:
            pass
        else:
            print("I think your seat is near " + str(seat_id))

    

    
    