import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 1025))

while True:
    cmessage = input("Enter number: ")
    c.send(cmessage.encode("utf-8"))
    
    if not cmessage:
        break
    responce = c.recv(2048)
    print (responce.decode("utf-8"))

c.close()