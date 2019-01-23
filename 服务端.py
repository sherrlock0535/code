# -*- coding: utf-8 -*-
import socket
import threading
import time
def tcplink(sock, addr):
    print('与对方连接成功')
    ma = '与对方连接成功'
    sock.send(ma.encode('utf-8'))
    while True:
        print('等待对方输入...')
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print(data.decode('utf-8'))
        data = input('现在是您输入: ')
        sock.send(data.encode('utf-8'))
    sock.close()
    print('连接中断.' % addr)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 6666))
s.listen(10)
print('等待对方连接...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
