


alphabet = map(chr, range(97, 123))

def SimpleSymbols(str): 
  array = list(str)
  for i in range(0, len(array)):
      try:
          index = alphabet.index(array[i])
          if i == 0:
              return 'false'
      except ValueError:
          continue
      
      if array[i+1] != '+' or array[i-1] != '+':
          return 'false' 
  return 'true'

    

#str = '+d+=3=+s+'
str = "f++d+"
print SimpleSymbols(str)  

