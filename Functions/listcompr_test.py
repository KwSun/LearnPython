'''
Created on 2015年10月15日

@author: apple
'''

a = [x*x for x in range(1,11) if x % 2 == 0]
print(a)

b = [m + n for m in 'ABC' for n in 'XYZ']
print(b)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])