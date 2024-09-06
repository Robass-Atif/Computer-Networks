
import socket

Host='10.5.124.126'
Port=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    s.sendall(b'tyyaab ')
    data = s.recv(1024)

print('Received', repr(data))
