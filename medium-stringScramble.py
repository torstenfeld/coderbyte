
alphabet = map(chr, range(97, 123))

def StringScramble(str1, str2):
    #str1 = re.sub(r'\W+', '', str1)
    #str2 = re.sub(r'\W+', '', str2)
    strList1 = list(str1)
    strList2 = list(str2)
    if len(str1) != len(str2):
        return 'false'
    
    sortedList1 = GetListOrderedByAlphabet(strList1)
    sortedList2 = GetListOrderedByAlphabet(strList2)
    if sortedList1 == sortedList2:
        return 'true'
    else:
        return 'false'

def GetListOrderedByAlphabet(strList):
    numList = []
    specialList = []
    charList = []
    for i in range(0, len(strList)):
        try:
            index = alphabet.index(strList[i])
        except ValueError:
            specialList.append(strList[i])
            continue
        charList.append(strList[i])
        numList.append(index)
    
    specialList.sort()
    bothLists = zip(charList, numList)
    bothLists.sort()
    sortedStr, sortedNums = zip(*bothLists)
    sortedList = list(sortedStr)

    for j in range(0, len(specialList)):
        sortedList.append(specialList[j])
    return sortedList


str1 = "abcgggdfe"
str2 = "abcdef"
print StringScramble(str1, str2)