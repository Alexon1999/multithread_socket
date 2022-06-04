import socket
import sys
from utils import *
from _thread import *

ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSideSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# host = '127.0.0.1'
host = '0.0.0.0'

try:
    port = int(sys.argv[1])
except:
    port = 8000
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print(f'\033[92mSocket is listening on {host}:{port}\033[0m')

ServerSideSocket.listen(5)
while True:
    try:
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    except:
        ServerSideSocket.close()

ServerSideSocket.close()