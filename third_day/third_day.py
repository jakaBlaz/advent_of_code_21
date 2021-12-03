def first_part():
    gamma_rate= 0
    epsilon_rate = 0
    input_array = []
    output_matrix = []
    xorMatrix = 0
    length_of_bytes = 0
    with open("third_day/input.txt",'r') as f:
        for i in f:
            input_array.append(int(i,2))
    length_of_bytes = len(str(bin(max(input_array)))[2:])
    for i in range(length_of_bytes):
        output_matrix.append(0)
        xorMatrix += 1 << i

    print(bin(xorMatrix))
    for j in input_array:
        for i in range(length_of_bytes):
            output_matrix[i] += (j & (1 << i)) >> i


    for i in range(len(output_matrix)):
        if output_matrix[i] > (len(input_array)/2):
            gamma_rate += 1 << i
        else:
            gamma_rate += 0 << i
    epsilon_rate = gamma_rate^xorMatrix
    return epsilon_rate*gamma_rate

def second_part():
    oxygen_array = []
    cO2_Scrubber_array = []
    input_array = []
    output_matrix = []
    length_of_bytes = 0
    with open("third_day/input.txt",'r') as f:
        for i in f:
            input_array.append(int(i,2))
    length_of_bytes = len(str(bin(max(input_array)))[2:])
    for i in input_array:
        output_matrix.append((i & (1 << (length_of_bytes-1))) >> (length_of_bytes-1))
    
    oxygen_array, cO2_Scrubber_array =  second_part_scrubber(input_array,output_matrix)
    j = 1
    while len(oxygen_array) > 1:
        output_matrix = second_part_extractor(oxygen_array,j, length_of_bytes)
        oxygen_array, tmp= second_part_scrubber(oxygen_array,output_matrix)
        j+= 1
    j = 1
    while len(cO2_Scrubber_array) > 1:
        output_matrix = second_part_extractor(cO2_Scrubber_array,j, length_of_bytes)
        tmp, cO2_Scrubber_array = second_part_scrubber(cO2_Scrubber_array,output_matrix)
        j += 1
    
    print(f'oxygen: {oxygen_array} and CO2: {cO2_Scrubber_array}')
    return oxygen_array[0] * cO2_Scrubber_array[0]

def second_part_scrubber(whole_array,row_array):
    oxygen_array, cO2_array = [[],[]]
    oxygen_rating, cO2_Scrubber_rating = [0,0]
    oxygen_criteria = 1
    if row_array.count(0) > row_array.count(1):
        oxygen_criteria = 0
    idx = 0
    for i in (row_array):
        if oxygen_criteria == i:
            oxygen_rating += 1
            oxygen_array.append(whole_array[idx])
        else:
            cO2_Scrubber_rating += 1
            cO2_array.append(whole_array[idx])
        idx += 1
    
    print(f'{oxygen_rating}, {cO2_Scrubber_rating}')
    print(f'{oxygen_array}, {cO2_array}')
    return oxygen_array, cO2_array

def second_part_extractor(input_array, idx, length_of_bytes):
    output_array = []
    length_of_bytes
    for i in input_array:
        output_array.append((i & (1 << (length_of_bytes-1-idx))) >> (length_of_bytes-1-idx))
    return output_array
print(second_part())
