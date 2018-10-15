#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, threading, time

def Tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection form %s:%s closed.' % addr

# step1: create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step2: bind a port for listening
host='127.0.0.1'
port=9999
s.bind((host,port))

# step3: waiting for connection
s.listen(5)
print "Waiting for connection"

# step4: accept a new socket connection
while True:
    sock, addr=s.accept()
# step5: run a thread to take charge of socket communication
    t = threading.Thread(target=Tcplink, args=(sock,addr))
    t.start()

