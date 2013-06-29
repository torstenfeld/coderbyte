
import itertools

def ArrayAddition(arr): 
    
    arr.sort()
    arr.reverse()
    sum = arr[0]
    del arr[0]
    stuff = arr
    
    for L in range(0, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            #print subset
            partSum = 0
            for i in range(0, len(subset)):
                partSum += subset[i]  
            
            if sum == partSum:
                return 'true'
    

    return 'false'

list = [4, 6, 23, 10, 1, 3]
print ArrayAddition(list)  


