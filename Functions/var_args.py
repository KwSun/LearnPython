'''
Created on 2015年10月14日

@author: apple
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

a = calc(1,2)
b = calc()
print(a)
print(b)
nums = [1,2,3]
c = calc(*nums)
print(c)

