

def find_first_factorial(int):
    result = 1
    if int < 2:
        return int
        
    for i in range(2, int+1):
        result *= i
    return result
    
integer = 4
result = find_first_factorial(integer)
print result