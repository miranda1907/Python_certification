def dfs(adjacency_matrix, node_label):
    visited = []
    stack = [node_label]


    while stack:
        current = stack.pop()
        if current in visited:
            continue
        else:
            visited.append(current)

        for column_i, edge in enumerate(adjacency_matrix[current]):
  
            if edge == 1:
                if column_i in visited:
                    continue
                else:
                    stack.append(column_i)             

    return visited

print(dfs([[0, 1, 0, 0],  [1, 0, 1, 0], [0, 1, 0, 1],[0, 0, 1, 0]], 1)) 

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3)) 
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3)) 
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3)) 
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0)) 
