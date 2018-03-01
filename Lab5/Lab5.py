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

gameList = ["Rock", "Paper", "Scissors"]
def server():
    # Create a socket object
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = socket.gethostname() # Get local machine name
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    while True:
        print("Listening...")
        c, addr = s.accept()    # Establish connection with client.
        print ("Got connecttion from", addr)
        serverPlay = input("Rock, Paper, Scissors? ")
        while serverPlay not in gameList:
            serverPlay = input("Try again! Rock, Paper, Scissors? ")

        while True:
            data = c.recv(1024) # Expected data drom client
            if not data:
                break           # If no data break

            clientPlay = data.decode('ascii')
            if clientPlay not in gameList:
                print ("Something went wrong! ")
                break

            answer = checkWinner(serverPlay, clientPlay)
            answer += "Server played {}, Client played {}".format(serverPlay, clientPlay)
            c.send(bytearray(answer,"ASCII"))  # Send data to client
            print (answer)

        c.close()               # Close the connection
        print ('client {} disconnected'.format(addr))


def client():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345

    s.connect((host, port)) # Connect to server
    play = input("Rock, Paper, Scissors? ")
    while play not in gameList:
        play = input("Try again! Rock, Paper, Scissors? ")

    s.send(bytearray(play, 'ASCII'))
    print('Sent: ', play)

    data = s.recv(1024)
    print(data.decode('ascii'))
    s.close()


def checkWinner(Server, Client):
    if Server == "Rock":
        if Client == "Paper":
            return "Client wins!"
        else:
            return "Server wins!"
    elif Server == "Paper":
        if Client == "Scissors":
            return "Client wins!"
        else:
            return "Server wins!"
    elif Server == "Scissors":
        if Client == "Rock":
            return "Client wins!"
        else:
            return "Server wins!"
