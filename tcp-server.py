import socket
import threading

host_ip="127.0.0.1"
host_port=9898
 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host_ip,host_port))
server.listen(5)
print(f"[*] listening on {host_ip}:{host_port}")

#client handling thread

def client_handler(client_socket):
    #print client data
    request=client_socket.recv(4096)
    print(F"[*] Recieved:{request}")

    #send back packet
    client_socket.send(b"Hi from server !")
    client.close()
while True:
    client,addr=server.accept()
    print(F"[*] Accepted connections from : {addr[0]}:{addr[1]}")\

    #start the client thread to handle incoming data
    client_handler=threading.Thread(target=client_handler,args=(client,))
    print("Starting the client handler !")
    client_handler.start()