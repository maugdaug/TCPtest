#!/usr/bin/env python3.6

import socket
import time
import pickle




HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.20', 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    testdict = {1: "Hey", 2: "There"}
    msg = pickle.dumps(testdict)
    

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(bytes(msg, "utf-8"))

   