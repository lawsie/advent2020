with open("input.txt") as f:
    data = f.readlines()

# Convert to 2d array otherwise the strings won't be mutable
data = [[char for char in n.strip()] for n in data]

#print("DATA -----------------")
#[print(n) for n in data]

# x, y coords for all check positions
def positions_to_check(x, y, data):

    #print("Examining x", x, "y",y)

    last_col = len(data[0])-1
    last_row = len(data)-1

    positions = [ [-1, -1], [0, -1], [1, -1],
                        [-1, 0], [1, 0],
                        [-1, 1], [0, 1], [1, 1]
    ]
    surroundings = []
    for position in positions:

        #print("Position ", str(position))

        # Start at x, y coordinates and look in the direction given
        x1 = x + position[0]
        y1 = y + position[1]

        seat_not_found = True

        while seat_not_found:

            #print("New x val", x1, "new y val", y1)

            # Check if this is still in bounds
            if x1 >= 0 and x1 <= last_row and y1 >= 0 and y1 <= last_col:
                # Assuming its in bounds, check if its a seat
                if data[x1][y1] == "L" or data[x1][y1] == "#":
                    #print("*** Found a ", data[x1][y1], " at ", x1, y1)
                    surroundings.append(data[x1][y1])
                    seat_not_found = False
                else:
                    # Move along a bit and try again
                    x1 += position[0]
                    y1 += position[1]
            else:
                # Out of bounds, so there must be only floor
                #print("Not a valid position")
                surroundings.append(".")
                seat_not_found = False

    return surroundings

def iterate(data):
    cols = len(data[0])
    rows = len(data)

    # Fill up new array with dummy values
    new_config = []
    any_changes = False
    
    # Loop through
    for row in range(rows):
        new_row = ["X" for i in range(cols)]
        for col in range(cols):
            # Get the positions to check
            surroundings = positions_to_check(row, col, data)
            #print(row, col, surroundings)
            
            # Make the changes to the new config
            if data[row][col] == "L" and "#" not in surroundings:
                new_row[col] = "#"
                any_changes = True
            elif data[row][col] == "#" and surroundings.count("#") >= 5:
                new_row[col] = "L"
                any_changes = True
            else:
                new_row[col] = data[row][col]
        new_config.append(new_row)

    if not any_changes:
        print("No changes")
        occupied_seats = 0
        for i in new_config:
            occupied_seats += i.count("#")
        print(occupied_seats)
        return False
    else:
        return new_config
    
# Make a copy of newdata to initialise
newdata = data.copy()

#print("COPY OF DATA -----------------")
#[print(n) for n in newdata]

while newdata is not False:
    newdata = iterate(newdata)
    #print("ITERATION -----------------")
    #[print(n) for n in newdata]

