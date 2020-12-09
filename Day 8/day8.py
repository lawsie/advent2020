with open("input.txt") as f:
    data = f.readlines()

# Get rid of newlines and make each into a list
data = [n.strip().split(" ") for n in data]

acc = 0
cir = 0
used_instructions = []

while cir not in used_instructions:
    print("Executing instruction " + str(cir))
    used_instructions.append(cir)

    # Get the instruction and the argument
    instruction = data[cir][0]
    arg = int(data[cir][1])

    if instruction == "acc":
        # Add the arg to the accumulator and move on
        acc += arg
        cir += 1
    elif instruction == "jmp":
        cir += arg
        pass
    elif instruction == "nop":
        # Just go to the next instruction
        cir += 1
    else:
        print("What's going on here")


print("Not going to execute ", cir, " again")
print("Accumulator is ", acc)
