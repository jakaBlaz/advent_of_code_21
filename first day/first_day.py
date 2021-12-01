initial_measurement_array = []
larger = 0
smaller = 0

f = open("input.txt", "r")
for i in f:
    initial_measurement_array.append(int(i))
# print((initial_measurement_array))

for i in (range(2,len(initial_measurement_array)-1)):
    a = initial_measurement_array[i-2] + initial_measurement_array[i-1] + initial_measurement_array[i]
    b = initial_measurement_array[i-1] + initial_measurement_array[i] + initial_measurement_array[i+1]
    if(b > a):
        larger += 1
    else:
        smaller += 1
        
print(f'smaller values : {smaller}')
print(f'larger values : {larger}')
print(f'(larger - smaller) values : {larger + smaller}')
