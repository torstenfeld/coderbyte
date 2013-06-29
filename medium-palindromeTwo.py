
import re

def PalindromeTwo(sen):
    sen = re.sub(r'\W+', '', sen)
    sen = sen.lower()
    strList = list(sen)
    strListReversed = strList 
    strListReversed.reverse()
    strReversed = ''.join(strListReversed)
    if strReversed == sen:
        return 'true'
    else:
        return 'false'


#sen = "Noel - sees Leon"
sen = "A war at Tarawaa!"
print PalindromeTwo(sen)