import socket # import socket module

def start():
    ans = input("Vill du köra som klient eller server? (K/S)")
    ans = ans.lower()
    while ans not in {"k", "s"}:
        ans = input("Fel input prova igen!")
        ans = ans.lower()

    if ans == "k":
        client()
    else:
        server()

gameList = ["O", "U", "X"]
def server():
    # Create a socket object
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = socket.gethostname() # Get local machine name
    print (host)
    port = 60003                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    serverscore, clientscore = 0,0

    s.listen(5)                 # Now wait for client connection.
    while True:
        print("Listening...")
        client, addr = s.accept()    # Establish connection with client.
        print ("Got connecttion from", addr)
        print ("If you want to quit type quit")
        while True:
            serverPlay = input("Rock, Paper, Scissors? (O,U,X) ").upper()
            if "QUIT" in serverPlay:
                break
            while serverPlay not in gameList:
                serverPlay = input("Try again! Rock, Paper, Scissors? (O,U,X) ").upper()

            data = client.recv(1024) # Expected data drom client
            if not data:
                break           # If no data break

            clientPlay = data.decode('ascii')
            answer = checkWinner(serverPlay, clientPlay)
            if "Server" in answer:
                serverscore += 1
            elif "Client" in answer:
                clientscore += 1

            # Skriver ut vad båda spelarna har spelat
            answer += (" Server played {}, Client played {}".format(serverPlay, clientPlay))
            # Skriver ut spelomgången:
            clientAnswer, serverAnswer = gamePrint(answer, serverscore, clientscore)
            #Nollställer om någon av spelarna vunnit:
            if serverscore >= 10 or clientscore >= 10:
                serverscore, clientscore = 0,0

            # Skickar omgången till klienten
            client.send(bytearray(clientAnswer,"ASCII"))  # Send data to client
            print (serverAnswer)

        client.close()               # Close the connection
        print ('client {} disconnected'.format(addr))


def client():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # host = input("Type hostname/ip: ")
    host = socket.gethostname()
    # port = input ("Type Portnr: ")
    port = 60003
    s.connect((host, port)) # Connect to server
    print ("If you want to quit type quit")
    while True:
        play = input("Rock, Paper, Scissors? (O,U,X)").upper()
        if "QUIT" in play:
            break
        while play not in gameList:
            play = input("Try again! Rock, Paper, Scissors? (O,U,X)").upper()

        s.send(bytearray(play, 'ASCII'))
        print('Sent: ', play)

        data = s.recv(1024)
        print(data.decode('ascii'))
    s.close()


def checkWinner(Server, Client):
    if Server == Client:
        return "Tie"
    if Server == "O":
        if Client == "U":
            return "Client wins!"
        else:
            return "Server wins!"
    elif Server == "U":
        if Client == "X":
            return "Client wins!"
        else:
            return "Server wins!"
    elif Server == "X":
        if Client == "O":
            return "Client wins!"
        else:
            return "Server wins!"

def gamePrint (answer, serverscore, clientscore):
    clientAnswer, serverAnswer = answer, answer
    if clientscore >= 10:
        clientAnswer = "You won! {} to {}".format(clientscore, serverscore)
        serverAnswer = "You lost! {} to {}".format(serverscore, clientscore)

    elif serverscore >= 10:
        clientAnswer += "You lost! {} to {}".format(clientscore, serverscore)
        serverAnswer += "You won! {} to {}".format(serverscore, clientscore)

    else:
        clientAnswer += "\nServer score: {}, Client score: {}".format(serverscore, clientscore)
        serverAnswer += "\nServer score: {}, Client score: {}".format(serverscore, clientscore)

    return clientAnswer, serverAnswer


start()
