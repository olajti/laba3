import socket
import ssl

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Підключаємося до сервера з перевіркою сертифікату
    client_ssl_socket = ssl.wrap_socket(client_socket, keyfile="client_private.key", certfile="client_certificate.pem", server_side=False, cert_reqs=ssl.CERT_OPTIONAL, ssl_version=ssl.PROTOCOL_TLS)
    
    client_ssl_socket.connect(('localhost', 12345))
    client_ssl_socket.sendall(b'Hello from client')
    data = client_ssl_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
    
    client_ssl_socket.close()

if __name__ == '__main__':
    client_program()
