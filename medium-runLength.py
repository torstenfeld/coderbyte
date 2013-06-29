

def RunLength(sen):
    result = ''
    strList = list(sen)
    
    count = 0
    lastChar = ''
    for i in range(0, len(strList)):
        char = strList[i]
        if lastChar == '':
            lastChar = char
            count += 1
            continue
        if char != lastChar:
            result = result + str(count) + lastChar
            lastChar = char
            count = 1
            continue
        else:
            count += 1
    result = result + str(count) + lastChar
    return result


sen = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print RunLength(sen)