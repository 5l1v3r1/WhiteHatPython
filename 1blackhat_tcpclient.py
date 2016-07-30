#tcp client
import socket

target_host = "127.0.0.1" #"www.google.com"
target_port = 8888

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print client
#connect to host
client.connect((target_host,target_port))
#send some 
client.send("GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
#recive response
response = client.recv(4096)
print response
