

def ArithGeo(list):
    
    step = 0
    result = 'Geometric' # for geometric
    
    # geo check
    for i in range(1, len(list)):
        newStep = list[i] / list[i-1]
        if step == 0:
            step = newStep
        else:
            if step == newStep:
                continue
            else:
                result = 'Arithmetic'
                break
    
    if result == 'Geometric':
        return result
    
    step = 0
    # arit check
    for i in range(1, len(list)):
        newStep = abs(list[i]-list[i-1])
        if step == 0:
            step = newStep
        else:
            if step == newStep:
                continue
            else:
                result = -1
                break
    
    return result
    

list = [1,2,4,8,16,3]
#list = [2,4,6,8]
print ArithGeo(list)