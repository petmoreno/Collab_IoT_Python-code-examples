import socket

ipaddress ='127.0.0.1'
localEndPoint =10001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
    listener.bind((ipaddress, localEndPoint))
    listener.listen()
    print('Waiting for a connection...')
    conn, addr=listener.accept()
    with conn:
        print('Connecty by', addr)
        data=''
        bytesRec=None
        while True:
            bytesRec=conn.recv(1024)
            #if not bytesRec:
            #    break
            data= data + bytesRec.decode ('utf-8') 
            if '<EOF>' in data:    
                break
        print('Text received: {0}',data)
        msg=data.encode('utf-8')
        conn.sendall(msg)
            #conn.sendall(bytesRec)