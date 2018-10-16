#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

# step1: create socket based socket type
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
        print "Failed to create socket"
        sys.exit()

print "Socket Created"

host='127.0.0.1'
ip=9999

# step2: start to connect
s.connect((host,ip))

# step3: communicate with remote server
print s.recv(1024)
for data in ['Michael','Tracy','Sarah']:
        try:
                s.send(data)
        except socket.error:
                print "Send Failed"
                sys.exit()
        print s.recv(1024)

try:
        s.send('exit')
except socket.error:
        print "Send Failed"
        sys.exit()

# step4: close socket
s.close()


