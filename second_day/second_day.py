def first_part():
    direction = ""
    value = 0
    depth = 0
    horizontal = 0
    with open("input.txt",'r') as f:
        for i in f:
            direction, value =  i.split(" ")
            value = int(value)
            if direction == "forward":
                horizontal += value
            elif direction == "down":
                depth += value
            elif direction == "up":
                depth -= value
    return depth*horizontal

def second_part():
    direction = ""
    value = 0
    depth = 0
    horizontal = 0
    aim = 0
    with open("input.txt",'r') as f:
        for i in f:
            direction, value =  i.split(" ")
            value = int(value)
            if direction == "forward":
                horizontal += value
                depth += aim * value
            elif direction == "down":
                aim += value
            elif direction == "up":
                aim -= value
    return depth*horizontal

print(f"The answer to the first part is: {first_part()}")
print(f"The answer to the first part is: {second_part()}")
