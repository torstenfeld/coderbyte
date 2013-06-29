

vowels = ['a', 'e', 'i', 'o', 'u']


def VowelCount(str):
    strList = list(str)
    resultList = []
    for i in range(0, len(strList)):
        test = strList[i].lower()
        try:
            index = vowels.index(test)
        except ValueError:
            continue
        resultList.append(test)
    return len(resultList)


str = "codErbyte"
print VowelCount(str)

