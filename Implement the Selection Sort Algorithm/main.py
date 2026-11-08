def selection_sort(array):
    if len(array) <= 1:
        return array

    for i in range(len(array)):   
  
        smallest_index = array.index(min(array[i:]), i)
        print(smallest_index)

        if array[i] != array[smallest_index]:
            array[i], array[smallest_index] = array[smallest_index], array[i]     
 

    return array


print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
