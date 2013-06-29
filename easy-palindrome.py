


def Palindrome(str):
    str = str.replace(" ", "")
    print str
    strList = list(str)
    strListReversed = strList 
    strListReversed.reverse()
    strReversed = ''.join(strListReversed)
    if strReversed == str:
        return 'true'
    else:
        return 'false' 

str = "never odd or even"
print Palindrome(str)