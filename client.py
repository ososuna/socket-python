import socket

HOST = '192.168.56.1'
PORT = 65123

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  s.sendall(b'Shutdown')
  data = s.recv(1024)
print('Received', repr(data))