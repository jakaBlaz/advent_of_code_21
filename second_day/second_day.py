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
            
print(f'depth is {depth}')
print(f'with a horizontal distance of {horizontal}')
print(f' Multiplied together they are {depth * horizontal}')
