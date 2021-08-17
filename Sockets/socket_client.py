import socket
import threading
import pandas as pd



ipaddress ='127.0.0.1'
localEndPoint =10001

def ReceiveData(client):
    #data='test'
    data=client.recv(1024)
    print('Received', repr(data.decode ('utf-8')))
    messagefromServer.set()
    
    
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((ipaddress,localEndPoint))
    print('client connected!!')
    messagefromServer=threading.Event()
    thread=threading.Thread(target=ReceiveData, args=(client,), daemon=True)
    thread.start()
    s=''
    while (not(pd.isnull(s))):
        s=input()
        buffer=s.encode('utf-8')
        client.sendall(buffer)
        if messagefromServer.is_set():
            break
    print('disconnect from server!!')    

