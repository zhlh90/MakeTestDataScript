# requests -> urlib ->socket
import socket
from urllib.parse import urlparse


IpPort7012 = '10.10.64.204:7012'
IpPort7012_bank = '192.168.50.93:7090'

def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send(F"GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection:close\r\n\r\n".encode("utf-8"))
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf-8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == '__main__':
    while True:
        print('\r\nplease import Port or quit.')
        port = input('Port:')
        if port == 'quit':
            break
        elif port == '7012':
            url = "http://" + IpPort7012_bank + "/sendToSServer/bankReturn"
            # get_url(url)
            print(url)
        else:
            print('no ' + port)

