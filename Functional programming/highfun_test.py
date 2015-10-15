'''
Created on 2015年10月15日

@author: apple
'''

def add(x, y, f):
    return f(x) + f(y)

a = add(-1,8,abs)
print(a)