import ssl
import socket

# Load server's certificate and private key
server_cert = 'ca/server_certificate.pem'
server_key = 'ca/server_private.key'

# Set up server socket
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.verify_mode = ssl.CERT_OPTIONAL  # Optional: Use CERT_REQUIRED for stricter verification

# Bind to a port and listen for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('localhost', 10023))
    sock.listen(5)
    print("Server listening on port 10023...")
    
    while True:
        client_socket, addr = sock.accept()
        with client_socket:
            print("Connection from", addr)
            
            # Wrap the socket for SSL communication
            ssl_socket = context.wrap_socket(client_socket, server_side=True)
            data = ssl_socket.recv(1024)
            print(f"Received from client: {data.decode()}")
            
            ssl_socket.send(b"Hello, Client!")