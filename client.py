# -*- coding: utf-8 -*-
import socket

PORT = 65123

HOST = input('Enter host: ')
cad = input('Enter message: ')
data = cad.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(data)
  data = s.recv(1024)
print('Received', repr(data))