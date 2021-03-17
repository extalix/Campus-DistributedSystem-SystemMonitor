from socket import *

addr = ('127.0.0.1', 5005)

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(addr)
    s.listen()
    conn, source = s.accept()

    with conn:
        print("connected by ", source)