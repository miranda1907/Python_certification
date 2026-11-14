def adjacency_list_to_matrix(adjacency_list):
    
    matrix_length = len(adjacency_list)

    adjacency_matrix = [[0] * matrix_length  for _ in range(matrix_length)]


    for row in adjacency_list:   

        for edge in adjacency_list[row]:  
            adjacency_matrix[row][edge] = 1


    for row in adjacency_matrix:
        print(row)  
  
    return adjacency_matrix

print(adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}) ) 
print(adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})) 
print(adjacency_list_to_matrix({0: [], 1: [], 2: []})) 
