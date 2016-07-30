import socket,threading

bind_ip = "0.0.0.0"
bind_port = 8888

#create a socket object 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#binding and listening 
server.bind((bind_ip,bind_port))
server.listen(5)#5 is the number of connecttion that we can save in queue
print "[*]Listening on %s:%d\r\n" %(bind_ip,bind_port)
#client handling
def  handle_client(client_socket):
    #recive client request
    client_request = client_socket.recv(4096)
    print "[*]Client Request:%s\r\n"%client_request
    #send ack to client as its response
    client_socket.send("ACK")
    client_socket.close()
    
#accept incoming connections(sockets)
while True:
    client, addr=server.accept()#server.accept() output is a collection of {[socket object],[socket(ip,port)]}: (<socket._socketobject object at 0x02E3C998>, ('127.0.0.1', 25129))
    print "[*]Accepted connection from %s:%s"%(addr[0],addr[1])
    
    #spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
    
    
