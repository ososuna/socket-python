# -*- coding: utf-8 -*-
import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 65123
out = False

while not out:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server is listening on {}:{}'.format(HOST, PORT))
    conn, addr = s.accept()
    with conn:
      print('Connected by', addr)
      while True:
        data = conn.recv(1024)
        if not data:
          break
      if data == bytes('Shutdown', 'utf-8'):
        out = True
        break
      msg = HOST + ':' + str(PORT)
      data = msg.encode(encoding='utf-8')
      print('Sending data:', repr(data))
      conn.sendall(data)
    if out:
      conn.close()
      print('Server is shutting down')
      break