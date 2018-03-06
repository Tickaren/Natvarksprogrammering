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
        while True:
            client.send(bytearray(
            str(clientscore) +","+ str(serverscore), "ascii"))

            #Nollställer om någon av spelarna vunnit:
            if serverscore >= 10 or clientscore >= 10:
                serverscore, clientscore = 0,0

            print("({},{}) Your move:".format(serverscore, clientscore))
            serverPlay = input().upper()
            while serverPlay not in gameList:
                serverPlay = input(
                "Try again! Rock, Paper, Scissors? (O,U,X) ").upper()

            data = client.recv(1024) # Expected data drom client
            if not data:
                break           # If no data break
            client.send(bytearray(serverPlay,"ASCII"))  # Send data to client
            clientPlay = data.decode('ascii')
            winner = checkWinner(serverPlay, clientPlay)
            if "Server" in winner:
                serverscore += 1
            elif "Client" in winner:
                clientscore += 1
            totalscorecheck(serverscore, clientscore)

        client.close()               # Close the connection
        print ('client {} disconnected'.format(addr))


def client():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = input("Type hostname/ip: ")
    # host = socket.gethostname()
    port = 60003
    s.connect((host, port)) # Connect to server
    while True:
        score = s.recv(1024)
        clientscore, serverscore = score.decode("ascii").split(",")
        totalscorecheck(int(clientscore), int(serverscore))

        print("({},{}) Your move:".format(clientscore, serverscore))
        play = input().upper()
        while play not in gameList:
            play = input("Try again! Rock, Paper, Scissors? (O,U,X)").upper()

        s.send(bytearray(play, 'ASCII'))

        clientmove = s.recv(1024)
        print("(Oponents move: " + clientmove.decode("ascii") +")")
    s.close()


def checkWinner(Server, Client):
    if Server == Client:
        return "Tie"
    if Server == "O":
        if Client == "U":
            return "Client"
        else:
            return "Server"
    elif Server == "U":
        if Client == "X":
            return "Client"
        else:
            return "Server"
    elif Server == "X":
        if Client == "O":
            return "Client"
        else:
            return "Server"

def totalscorecheck(score1, score2):
    if score1 >= 10:
        print("You won with {} against {}".format(score1, score2))
    elif score2 >= 10:
        print("You lost with {} against {}".format(score1, score2))

start()
