import socket
import select

# Sends data to all klients in listOfSockets
def broadcast(sock, message):
    for s in listOfSockets:
        if s is not server_socket and s is not sock:
            try:
                s.send(bytearray(message, "ASCII"))
            except:
                s.close()
                listOfSockets.remove(s)
                print("Send failed")

port = 60003
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", port))
server_socket.listen(10)

listOfSockets = [server_socket]
listOfSockets.append(server_socket)

print ("Lyssnar på port {}".format(port))

while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    # If new client:
    if sock == server_socket:
        Sockclient, addr = server_socket.accept()
        print ("New connection from:", addr)
        listOfSockets.append(Sockclient)
        broadcast(Sockclient, "{} (Connected)".format(addr))
    else:
        # Existing client that sends message or disconects!
        data = sock.recv(2048)
        if not data: # disconnected client
            broadcast(sock, "{} (Nedkopplad)".format(addr))
            print("klient ({}) är offline".format(addr))
            sock.close()
            listOfSockets.remove(sock)
        else: # Recived message from client
            broadcast(sock, "\r" + "<" + str(sock.getpeername()) + ">" + data.decode("ASCII"))
