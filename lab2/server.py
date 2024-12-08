import socket

def run_server():
    # Create a socket object (IPv4, TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define server IP and port (localhost and port 8000)
    server_ip = "10.5.124.140"
    port = 8000
    
    # Bind the server socket to the IP and port
    server.bind((server_ip, port))
    
    # Start listening for incoming connections (backlog of 0, meaning no queued connections)
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")
    
    # Accept a new client connection
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    # Main loop to receive and process client requests
    while True:
        # Receive data from the client (1024-byte buffer size)
        request = client_socket.recv(1024)
        
        # Decode the received bytes to a string
        request = request.decode("utf-8")
        
        # Check if the client requested to close the connection
        if request.lower() == "close":
            # Send a "closed" message back to the client and break the loop
            client_socket.send("closed".encode("utf-8"))
            break
        
        # Print the received message
        print(f"Received: {request}")
        
        # Send a response back to the client acknowledging receipt
        response = "accepted".encode("utf-8")
        client_socket.send(response)
    
    # Close the connection with the client
    client_socket.close()
    print("Connection to client closed")
    
    # Close the server socket
    server.close()

# Run the server
run_server()
