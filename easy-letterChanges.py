
import string

alphabet = map(chr, range(97, 123))
vowels = ['a', 'e', 'i', 'o', 'u']
#str = "hello*3"
str = "fun times!"

def LetterChanges(str):
    result = []
    str = str.lower()
    array = list(str);

    for i in range(0, len(array)):
        try:
            index = alphabet.index(array[i])
        except ValueError:
            result.append(array[i])
            continue
        
        if array[i] == 'z':
            new_char = 'a'
        else:
            new_char = alphabet[index+1]
        
        try:
            index_vowel = vowels.index(new_char)
            new_char = new_char.upper()
        except ValueError:
            result.append(new_char)
            continue
        result.append(new_char)
    result = ''.join(result)
    return result

    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down

#str = "fun times!"
print LetterChanges(str)  



