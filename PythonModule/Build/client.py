#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 6001        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for _ in range(30):
        s.sendall(b'UP')
        time.sleep(0.1)
    data = s.recv(1024)
    s.sendall(b'STOP')

print('Received', repr(data))
