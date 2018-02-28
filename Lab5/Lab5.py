import socket # import socket module

class mysocket:
    def server():
        s = socket.socket           # Create a socket object
        host = socket.gethostname() # Get local machine name
        port = 12345                # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port
        
        s.listen(5)                 # Now wait for client connection.
        while True:
            c, addr = s.accept()    # Establish connection with client.
            print ("Got connecttion from", addr)
            c.send(bytearray("Thank you for connecting","ASCII"))
            c.close()               # Close the connection


    def client():
        s = socket.socket()
        host = socket.gethostname()
        port = 12345

        s.connect((host, port))
        print(s.recv(1024))
        s.close
