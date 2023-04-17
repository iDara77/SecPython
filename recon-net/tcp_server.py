import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

server.bind((host, port))
server.listen(5)

print(f"Running TCP server on {host}:{port}")
while True:
    client, address = server.accept()
    print(f"Received connection from {client} {address}")
    message = "Hello!\r\n"
    client.send(message.encode('ascii'))
    print(f"Sent TCP to {client} {address}")
    client.close()
    print(f"Closed TCP with {client} {address}")