import socket

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

host = socket.gethostname()
port = 666

print(f"Sending UDP to {host}:{port} ")
client.sendto(b'Banner query\r\n',(host,port))
print(f"Waiting for response...")
message = client.recvfrom(1024)
print(f"Received from {host}:{port} : {message}")