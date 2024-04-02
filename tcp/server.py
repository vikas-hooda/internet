# server.py

import socket

HOST = "127.0.0.1"  # (localhost)
PORT = 65432  # Random port
#socket.SOCK_STREAM is for TCP and socket.SOCK_DGRAM is for UDP
#AF stands for Address Family, INET is for IPv4
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        all_data=b''
        print(f"Connection from  {addr}")
        #Chrome sends Connection:keep-alive so it will not exit this loop but with normal python client it will exit once no data
        while True:
            print('###')
            data = conn.recv(1000)
            print(data)
            if not data:
                break
            all_data+=data
        print(all_data) 
        
            
            