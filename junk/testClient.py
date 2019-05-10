import socket

HOST = '192.168.1.106'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello maaneneeen')
    data = s.recv(1024)
print('Received', repr(data))
		
		