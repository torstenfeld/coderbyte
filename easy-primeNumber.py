


def CheckForPrime(num):
    maxDivider = num / 2
    if num % 2 != 0:
        maxDivider = (num - 1) / 2
    
    for i in range(2, maxDivider + 1):
        if num % i == 0:
            return 'false'
    return 'true'
        
    
    
num = 12
print CheckForPrime(num)