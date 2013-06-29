

def Division(num1, num2):
    maxDivider1 = GetMaxDivider(num1)
    maxDivider2 = GetMaxDivider(num2)
    
    dividerListNum1 = GetListOfDividers(num1, maxDivider1)
    dividerListNum2 = GetListOfDividers(num2, maxDivider2)
    print dividerListNum1
    print dividerListNum2
    
    return FindHighestMatchOfTwoList(dividerListNum1, dividerListNum2)

def GetMaxDivider(num):
    maxDivider = num / 2
    if num % 2 != 0:
        maxDivider = (num - 1) / 2
    return maxDivider

def GetListOfDividers(num, maxDivider):
    resultList = []
    
    for i in range(2, maxDivider+1):
        if num % i == 0:
            resultList.append(i)
    return resultList

def FindHighestMatchOfTwoList(list1, list2):
    match = 1
    if len(list1) > len(list2):
        shortList = list2
        longList = list1
    else:
        shortList = list1
        longList = list2
        
    shortList.reverse()
    longList.reverse()
    
    for i in range(0, len(shortList)):
        try:
            index = longList.index(shortList[i])
        except ValueError:
            continue
        if match < shortList[i]:
            match = shortList[i]
    
    return match

num1 = 50
num2 = 100
print Division(num1, num2)