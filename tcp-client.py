import socket

#setting target host 
target_host="127.0.0.1"
target_port=9898
#creating socket object
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connecting to the server
client.connect((target_host,target_port))
#sending data
client.sendall(b"here is the client message !")
#receive data
response=client.recv(4096)
print(response)
