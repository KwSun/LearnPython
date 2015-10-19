'''
Created on 2015年10月19日

@author: apple
'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'kw', b'fx', b'lhj']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()