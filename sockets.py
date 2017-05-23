#simple socket
import socket


print("Starting Socket client")
s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))

print(s.recv(1024))

s.close()

print("Terminated Socket Client")