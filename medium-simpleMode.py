

def SimpleMode(arr):
    listDistinct = Distinct(arr)
    count = []
    
   
    for iNumToSearch in range(0, len(listDistinct)):
        count.append(0)
        for iCurrNum in range(0, len(arr)):
            if arr[iCurrNum] == listDistinct[iNumToSearch]:
                count[iNumToSearch] += 1
    
    numMaxOccurence = -1
    maxOccurence = 0
    for i in range(0, len(count)):
        if count[i] > 1 and count[i] > maxOccurence:
            maxOccurence = count[i]
            numMaxOccurence = listDistinct[i]
    return numMaxOccurence

def Distinct(seq): 
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

array = [10, 4, 5, 2, 4]
print SimpleMode(array)