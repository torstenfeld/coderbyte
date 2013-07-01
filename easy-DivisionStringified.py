

def DivisionStringified(num1,num2):
    if num1 < num2:
        return '1' 
    result = str(num1 / num2)
    strList = list(result)
    strList.reverse()
    if len(strList) <= 3:
        return result
    
    resultList = []
    strResult = ''
    count = 0
    for i in range(0, len(strList)):
        count += 1
        resultList.append(strList[i])
        if count == 3:
            resultList.append(',')
            count = 0
    resultList.reverse()
    strResult = ''.join(resultList) 
    return strResult
    

num1 = 503394930
num2 = 43
print DivisionStringified(num1, num2)