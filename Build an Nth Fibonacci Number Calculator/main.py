def fibonacci(n):
    sequence = [0, 1]

    if n < len(sequence):
        return sequence[n]

    for num in range(len(sequence), n + 1):
        num = sequence[-1] + sequence[-2]
        sequence.append(num)

    return sequence[n]



print(fibonacci(0))
print(fibonacci(1)) 
print(fibonacci(2))
print(fibonacci(3))  
print(fibonacci(5))
print(fibonacci(10)) 
print(fibonacci(15))    
