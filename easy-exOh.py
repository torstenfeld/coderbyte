

def ExOh(str): 
    strList = list(str)
    aList = []
    bList = []
    
    aList = [i for i, x in enumerate(strList) if x == "x"]
    bList = [i for i, x in enumerate(strList) if x == "o"]
    
    if len(aList) != len(bList):
        return 'false'
    else:
        return 'true'
    
str = "xooxx"    
print ExOh(str)  