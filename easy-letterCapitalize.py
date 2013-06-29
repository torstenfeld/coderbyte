

def LetterCapitalize(str): 
    result_list = []
    split = str.split(' ')
    for i in range(0, len(split)):
        word_capitalized = split[i].capitalize()
        result_list.append(word_capitalized)
    result = ' '.join(result_list)
    return result
    
    
#str = "hello world"
str = "i ran there"
print LetterCapitalize(str)