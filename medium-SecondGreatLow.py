

def SecondGreatLow(arr):
    if len(arr) == 2 and arr[0] == arr[1]:
        return str(arr[0]) + ' ' + str(arr[1])
    
    arr = Distinct(arr)
    arr.sort()
    secondLowest = arr[1]
    secondLargest = arr[len(arr)-2]
    
    return str(secondLowest) + ' ' + str(secondLargest)

def Distinct(seq): 
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

arr = [7, 7, 12, 98, 106]
print SecondGreatLow(arr)