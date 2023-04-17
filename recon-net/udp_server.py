import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

host = socket.gethostname()
port = 666

server.bind((host, port))

print(f"Running UDP server on {host}:{port}")
while True:
    message, address = server.recvfrom(1024)
    print(f"Received UDP from {address} {message}")
    message = "Hello!\r\n"
    server.sendto(message.encode('ascii'),address)
    print(f"Sent UDP {address}")