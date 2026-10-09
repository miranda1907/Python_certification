def number_pattern(n):

    list = []
    
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    for num in range(1, n+1):
        list.append(str(num))

    return " ".join(list)

print(number_pattern(4)) 
print(number_pattern(12))   
