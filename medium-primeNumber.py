

def PrimeMover(num):
    primeNumbers = [2,3]
    isPrime = 1
    
    for i in range(4, 10001):
        maxDivider = i / 2
        if i % 2 != 0:
            maxDivider = (i - 1) / 2
    
        for j in range(2, maxDivider + 1):
            if i % j == 0:
                isPrime = 0
                break;

        if isPrime == 1:
            primeNumbers.append(i)
            if len(primeNumbers) == num:
                return i

        isPrime = 1


num = 100
print PrimeMover(num)