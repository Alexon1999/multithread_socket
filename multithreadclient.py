import socket
import sys

ClientMultiSocket = socket.socket()
#host = '127.0.0.1'
host = '0.0.0.0'
# 0.0.0.0 is a non-routable meta-address that also specifies all IP # addresses on all interfaces on the system


try:
    port = int(sys.argv[1])
except:
    port = 8000

print(f'\033[93mWaiting for connection response\033[0m')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
# res = ClientMultiSocket.recv(1024)

server = port

while True:
    try:
        if(not server) :
            server = int(input('Which Server (8000/8001/8002) ? '))
        print("\033[93mq : (talk to other servers)\033[0m")
        Input = input('Your Message : ')
        if Input == 'q':
            server = None
            continue
        ClientMultiSocket.send(str.encode((str(server) if server else '') + ':' + Input))
        print('🚀')
        res = ClientMultiSocket.recv(1024)
        msg = res.decode('utf-8')
        print(msg)
        if msg == '401':
            server = None
    except:
        ClientMultiSocket.close()
        break
        
ClientMultiSocket.close()