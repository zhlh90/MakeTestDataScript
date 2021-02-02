import socket

client = socket.socket()

ip_port = ('127.0.0.1',9999)

client.connect(ip_port)

while True:
    data = client.recv(1024).decode()
    print(data)
    inp = input('client:')
    client.send(inp.encode())
    if inp == 'exit':
        break

