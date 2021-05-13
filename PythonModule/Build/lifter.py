#! /usr/bin/python2

import time
import socket

from fotosfera import moveTo, getStatus, Up,Down,Stop


def listener(port=6001, host='127.0.0.1'):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(port)
            
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)

                if not data:
                    print("stop")
                    break

                task  = data.decode('UTF-8')

                if task=="UP":
                    print("UP we go")
                    Up()
                elif task=="DOWN":
                    print("DOWN we go")
                    Down()
                else:
                    print("stop")
                    Stop()
                    break

                    
                    

                    
    
                    
                conn.sendall(b'CLOSED')
        s.close()


    


listener(port=6001, host='127.0.0.1')
#print(getStatus())