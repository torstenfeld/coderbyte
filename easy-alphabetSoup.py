

#import numpy
alphabet = map(chr, range(97, 123))


def AlphabetSoup(str): 
    result = ''
    strList = list(str)
    numList = []
    for i in range(0, len(strList)):
        index = alphabet.index(strList[i])
        numList.append(index)
    
    bothLists = zip(strList, numList)
    bothLists.sort()
    sortedStr, sortedNums = zip(*bothLists)
    result = ''.join(sortedStr)
    return result

#str = "coderbyte"
str = "hooplah"
print AlphabetSoup(str)  