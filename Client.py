from socket import *

serv = ('127.0.0.1', 5005)

with socket() as sock:
    sock.connect(serv)
