import socket


ADDRESS = ('localhost', 80)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDRESS)
server.listen(1)
print('wait for connection...')

while True:
    client, addr = server.accept()
    print(f'At {addr}')

    response_status = 'HTTP/1.1 200 OK'
    msg = "<html>Hello World</html>"
    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(msg.encode()),
        'Connection': 'close',
    }
    response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in response_headers.items())  # noqa: E501

    client.send(response_status.encode())
    client.send(response_headers_raw.encode())
    client.send('\n'.encode())
    client.send(msg.encode())
    client.close()

server.close()
