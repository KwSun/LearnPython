'''
Created on 2015年10月17日

@author: apple
'''
# f = open('/Users/apple/Desktop/aaa.txt','r')
# f.read()
# f.close()
from datetime import datetime

with open('aaa.txt', 'w') as f:
    f.write('Today is ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('aaa.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('aaa.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)