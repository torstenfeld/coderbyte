



def TimeConvert(num): 
    hours = num / 60
    min = num % 60
    result = str(hours) + ':' + str(min) 
    return result
    
    
num = 45
print TimeConvert(num)