import socket
import select

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

    if sock == server_socket:
        Sockclient, addr = server_socket.accept()
        print ("New connection from:", addr)
        # TODO ny klient ansluter sig.
        # anropa (Sockclient, addr) = sockL.accept() och ta hand om den nya klienten
        # stoppa in klientens socket i socketlist
        listOfSockets.append(Sockclient)
        broadcast(Sockclient, "{} (Connected)".format(addr))
    else:
        # Befintlig klient skickar data eller kopplar ner
        data = sock.recv(2048)
        if not data:
            broadcast(sock, "{} (Nedkopplad)".format(addr))
            print("klient ({}) är offline".format(addr))
            sock.close()
            listOfSockets.remove(sock)
            # TODO hantera nedkoppling från sock
            # Stäng socketförbindelsen och ta bort sock från listan
        else:
            broadcast(sock, "\r" + "<" + str(sock.getpeername()) + ">" + data.decode("ASCII"))
            print("<" + str(sock.getpeername()) + ">" + data.decode("ASCII"))
            # TODO data är ett meddelande från klienten
            # skicka detta till alla klienter
