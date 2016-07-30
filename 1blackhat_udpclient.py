#udp client
import socket

target_host = "127.0.0.1"#"www.google.com"
target_port = 8000

#create a socket object 
udpclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#send some data ->(udp is connectionless)
udpclient.sendto("AAABBBCCC",(target_host,target_port))
#recive some data
data, addr=udpclient.recvfrom(4096)
print data
