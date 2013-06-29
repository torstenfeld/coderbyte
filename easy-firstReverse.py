#!/usr/bin/env python

def string_reverse(str):
    str_array = list(str)
    str_array.reverse()
    str_reversed = ''.join(str_array)
    return str_reversed
    
string_to_reverse = 'this is a test'
result = string_reverse(string_to_reverse)
print result
