import threading 

HEADER = 64
FORMAT = 'utf-8'

def send_mess(mess,connection):
    message = mess.encode(FORMAT)
    mess_length = len(mess)
    send_length = str(mess_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    connection.send(send_length)
    connection.send(message)

class send_round_mess(threading.Thread):

    def __init__(self, threadID, name,all_client_info,choice_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.all_client_info = all_client_info
        self.choice_list = choice_list

    def run(self):
        for x in self.all_client_info:
            string = "ROUND " + self.choice_list
            print(string, end = "")
            send_mess((string + "\n"),x[2])
            print("wysyla sie")
