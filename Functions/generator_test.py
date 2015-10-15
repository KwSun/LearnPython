'''
Created on 2015年10月15日

@author: apple
'''
g = (x * x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b
        n = n + 1
    return 'done'
# print(fib(6))
for n in fib(6):
    print(n)
    
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break