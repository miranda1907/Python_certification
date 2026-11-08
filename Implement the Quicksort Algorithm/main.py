def quick_sort(array):    
    if len(array) <= 1:
        return array

    sorted_list = []
    pivot = array[0]

    less_than = [element for element in array if element < pivot]
    greater_than = [element for element in array if element > pivot]
    equal = [element for element in array if element == pivot]

    sorted_less = quick_sort(less_than)
    sorted_greater = quick_sort(greater_than)

    return sorted_less + equal + sorted_greater



print(quick_sort([20, 3, 14, 1, 5]))  
print(quick_sort([83, 4, 24, 2]))   
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])) 
