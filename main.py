import socket
from stockfish_wrapper import get_best_move

HOST = "0.0.0.0"
PORT = 65432

def start_server(host=HOST, port=PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    
    server_socket.listen(5)
    print(f'Server listening on {host}:{port}')
    
    while True:
        client_socket, addr = server_socket.accept()
        #// print(f'Connection from {addr}')
        
        try:
            # dobimo podatke od roke
            data = client_socket.recv(1024).decode('utf-8') # 1MB max
            if not data:
                break
            #// print(f'Received data: {data}')
            
            response = get_best_move(data)
            if response == False:
                response = "Invalid FEN"
            #// print(f'Sending response: {response}')
            
            # Poslemo nazaj roki
            client_socket.sendall(response.encode('utf-8'))
        
        finally:
            client_socket.close()

if __name__ == "__main__":
    start_server()
