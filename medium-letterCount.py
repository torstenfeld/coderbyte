
alphabet = map(chr, range(97, 123))

def LetterCount(sen):
    listOfWords = sen.split(' ')
    
    wordFound = ''
    wordMax = 0
    
    for i in range(0, len(listOfWords)):
        maxInWord = GetHighestCharCount(listOfWords[i])
        if maxInWord > wordMax:
            wordMax = maxInWord
            wordFound = listOfWords[i]
            
    if wordMax <= 1:
        return -1
    else:
        return wordFound

def GetHighestCharCount(word):
    
    charsList = list(word)
    countList = []
    for j in range(0, len(alphabet)):
        countList.append(0)
    
    for i in range(0, len(charsList)):
        char = charsList[i].lower()
        try:
            index = alphabet.index(char)
        except ValueError:
            continue
        countList[index] += 1
    
    maxValue = 0
    for k in range(0, len(countList)):
        if countList[k] > maxValue:
            maxValue = countList[k] 
    
    return maxValue

sen = "Hello appple pie"
print LetterCount(sen)