#tcp server 
import socket,threading

bind_ip = "0.0.0.0"
bind_port = 8888

#create a socket object 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#binding and listenting
server.bind((bind_ip,bind_port))
server.listen(5)
print "[*]Listening on %s:%d"%(bind_ip,bind_port)
 
#client handling function
def handle_client(client_socket):
    request = client_socket.recv(4096)
    print "[*]Client request:%s"%request
    client_socket.send("ack!")
    client_socket.close()
    
while True:
    client,addr = server.accept()
    print "[*]accepted connection %s:%s"%(addr[0],addr[1])
    
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
    



