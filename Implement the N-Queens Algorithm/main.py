def dfs_n_queens(n):

    solutions = []

    if n < 1 or n == 2 or n == 3:
        return []
    elif n == 1:
        return [[0]]
    else:
        board = []

        def backtrack(row, board):
            if row == n:
                solutions.append(board.copy())
                return

            for col in range(n):
                if col in board:
                    continue

                is_safe = True

                for i, previous_col in enumerate(board):
                    if abs(row - i) == abs(col - previous_col):
                        is_safe = False
                        break 
                if is_safe == True:
                    board.append(col)  

                    backtrack(row + 1, board)
                    board.pop() 
        backtrack(0, board)                     


    return solutions 

print(dfs_n_queens(1))
print(dfs_n_queens(2))
print(dfs_n_queens(3)) 
print(dfs_n_queens(4))
print(dfs_n_queens(5))
print(dfs_n_queens(8))
print(len(dfs_n_queens(5)))
print(len(dfs_n_queens(8)))
   
