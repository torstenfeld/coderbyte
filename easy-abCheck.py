


def ABCheck(str): 
    strList = list(str)
    print strList
    aList = []
    bList = []
    
    aList = [i for i, x in enumerate(strList) if x == "a"]
    bList = [i for i, x in enumerate(strList) if x == "b"]
    print aList
    print bList
    if len(aList) == 0 or len(bList) == 0:
        return 'false'

    for i in range(0, len(aList)):
        for j in range(0, len(bList)):
            print abs(aList[i]-bList[j])
            if abs(aList[i]-bList[j]) < 3:
                return 'false'
    return 'true'
        
    
    
#str = "abccccazzzb"
str = "Laura sosb"
print ABCheck(str) 