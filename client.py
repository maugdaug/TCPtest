import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.20', 1238))


while True:

    full_msg = b''
    new_msg = True

    while True:
        msg = s.recv(HEADERSIZE)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            recvdobj = pickle.loads(full_msg[HEADERSIZE:])
            print(recevdobj)

            new_msg = True
            full_msg = b''
        
    print(full_msg)


