# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6666))
print(s.recv(1024).decode('utf-8'))
while True:
    data = input('现在是您输入: ')
    s.send(data.encode('utf-8'))
    print('等待对方输入')
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()