'''
Created on 2015年10月17日

@author: apple
'''
from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('L \n O \n V \n E')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
