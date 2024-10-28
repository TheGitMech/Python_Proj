import socket

target_IP = "127.0.0.1"
target_PORT = 9998

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_IP,target_PORT))

client.send(b"Helloo")

response = client.recv(2048)

print(response.decode())
client.close()