import socket

server_host='127.0.0.1'
server_port=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((server_host,server_port)) #Accepts a tuple containing the parameters
    s.sendall(b'Yo') # Accepts bytes 
