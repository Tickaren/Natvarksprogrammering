import socket
import select

port = 60003
sockL = socket.socket(socke.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(2)

listOfSockets = [sockL]

print ("Lyssnar på port {}".format(port))

while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:
        pass
        # TODO ny klient ansluter sig.
        # anropa (Sockclient, addr) = sock.accept() och ta hand om den nya klienten
        # stoppa in klientens socket i socketlist
    else:
        pass
        # Befintlig klient skickar data eller kopplar ner
        data = sock.recv(2048)
        if not data:
            pass
            # TODO hantera dedkoppling från sock
            # Stäng socketförbindelsen och ta bort sock från listan
        else:
            pass
            # TODO data är ett meddelande från klienten
            # skicka detta till alla klienter
