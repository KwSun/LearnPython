'''
Created on 2015年10月16日

@author: apple
'''

import functools
int2 = functools.partial(int, base=2)
a = int2('1000000')
print(a)