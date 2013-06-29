
import re

def find_largest_word(str):
    split = str.split(' ')
    largest_word = ''
    for i in range(0, len(split)):
        word_to_test = re.sub(r'\W+', '', split[i])  
        if len(word_to_test) > len(largest_word):
            largest_word = word_to_test
    return largest_word
    
#sentence = 'this is aaaaaaaaaaaaaaaaaaa reallybiglarge sentence'
sentence = "fun&!! time"
result = find_largest_word(sentence)
print result