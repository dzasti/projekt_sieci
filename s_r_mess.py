HEADER = 64
FORMAT = 'utf-8'
f = 0

def send_m(mess,connection):
    m1 = mess
    message = mess.encode(FORMAT)
    mess_length = len(mess)
    send_length = str(mess_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    connection.send(send_length)
    connection.send(message)
    append_to_log(m1,"S")

def recv_mess(connection):
     msg_length = connection.recv(HEADER).decode(FORMAT)
     msg_length = int(msg_length)
     msg = connection.recv(msg_length).decode(FORMAT)
     append_to_log(msg,"")
     return msg

def append_to_log(mess,role):
    global f
    f = open("communication_log.txt", "a")
    if role == "S":
        mess = "S: " + mess
    else:
        mess = "C: " + mess
    f.write(mess)
    f.close()

def create_file():
    global f
    f= open("communication_log.txt","w+")
    f.write("")
    f.close()