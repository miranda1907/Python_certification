def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]

    number_range = range_of_numbers(start_num, end_num - 1) 
    number_range.append(end_num) 

    return number_range

print(range_of_numbers(1, 5))  
print(range_of_numbers(6, 9))  
print(range_of_numbers(4, 4)) 
print(range_of_numbers(10,15)) 
print(range_of_numbers(1,3)) 
