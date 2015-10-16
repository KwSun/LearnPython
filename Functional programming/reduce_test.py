'''
Created on 2015年10月16日

@author: apple
'''
from functools import reduce
def f(x,y):
    return x * 10 + y
a = reduce(f, [1,2,3,4,5])
print(a)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

b = reduce(f,map(char2num,'12345')) 
print(b) 
       
