'''
Created on 2015年10月18日

@author: apple
'''

import subprocess


print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)