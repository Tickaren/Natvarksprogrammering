import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print ("{} wrote:".format(self.client_address[0]))
        print (self.data.decode("ascii"))

        # Sends the request back to the klient:
        self.request.sendall(bytearray("HTTP/1.1 200 ok\n", "ASCII"))
        self.request.sendall(bytearray("\n", "ASCII"))
        self.request.sendall(bytearray("<html>\n", "ASCII"))
        self.request.sendall(bytearray("<h1>Din request</h1>\n", "ASCII"))
        self.request.sendall(bytearray(
        "<p>Din klient skickade denna request:</p>\n", "ASCII"))
        self.request.sendall(bytearray("<pre>", "ASCII"))
        self.request.sendall(bytearray(self.data.decode("ascii"), "ASCII"))
        self.request.sendall(bytearray("</pre>", "ASCII"))
        self.request.sendall(bytearray("</html>\n", "ASCII"))


def startServer():
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), TCPHandler)

    # Activate the server; this will keep running until you
    server.serve_forever()

startServer()
