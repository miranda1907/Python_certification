def square_root_bisection(num, tolerance=0.01, maximum=10):

    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num
    else:
        low = 0
        high = max(1, num)

        for i in range(maximum):
            mid = (low + high) / 2

            if abs(high - low) <= tolerance:
                
                print(f"The square root of {num} is approximately {mid}")
                return mid
            
            elif mid ** 2 > num:
                high = mid
            else:
                low = mid

        print(f"Failed to converge within {maximum} iterations") 
        return None       
  
