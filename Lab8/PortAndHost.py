import tkinter
from Lab8 import start

def startchat(event=None):
    start(int(PORT.get()),str(HOST.get()))

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
HOST = tkinter.StringVar()  # For the messages to be sent.
PORT = tkinter.IntVar()

entry_field_host = tkinter.Entry(top, textvariable=HOST)
entry_field_host.bind("<Return>", startchat)
entry_field_host.pack()

entry_field_port = tkinter.Entry(top, textvariable=PORT)
entry_field_port.bind("<Return>", startchat)
entry_field_port.pack()
send_button = tkinter.Button(top, text="Send", command=startchat)
send_button.pack()

tkinter.mainloop()
