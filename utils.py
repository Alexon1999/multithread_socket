import socket

host = "0.0.0.0"

def multi_threaded_client(connection: socket.socket) -> None:
    # connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        if not data:
            break
        msg = data.decode('utf-8').split(':')
        port = int(msg[0])
        content = msg[1]
        clients_port = connection.getsockname()[1]
        if(port in (8000, 8001, 8002) and port != clients_port):
            send_to_server(connection, port, data)
        else:
            response = 'Server Message : ' +  input('Server Message : ')
            connection.sendall(str.encode(response))
    connection.close()


def send_to_server(connection: socket.socket, port: int, data: bytes) -> None:
    try:
        socket_ext_server = socket.create_connection((host, port))
        socket_ext_server.send(data)
        data2 = socket_ext_server.recv(2048)
        connection.sendall(data2)
        socket_ext_server.close()
    except ConnectionRefusedError:
        print(f'Connexion Refusé {host}:{port}')
        connection.sendall("401".encode('utf-8'))