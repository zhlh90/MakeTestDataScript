import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen()

while True:
    conn,address = sk.accept()
    conn.send('hello.'.encode())
    flag = True
    while flag:
        data = conn.recv(1024).decode()
        print(data)
        if data == 'exit':
            flag = False
        conn.send('hi'.encode())
    conn.close()
