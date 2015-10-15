'''
Created on 2015年10月15日

@author: apple
'''
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
    
for value in d.values():
    print(value)
    
for k,v in d.items():
    print(k,v)
    
for i,value in enumerate(['a','b','c']):
    print(i,value)
    
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
    

    
