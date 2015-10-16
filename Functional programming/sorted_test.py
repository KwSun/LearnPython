'''
Created on 2015年10月16日

@author: apple
'''

L = list( sorted([36, 5, -12, 9, -21], key=abs))
print(L)

S = list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
print(S)