'''
Created on 2015年10月17日

@author: apple
'''
from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '我爱Python'.encode('utf-8')
f = BytesIO(data)
print(f.read())