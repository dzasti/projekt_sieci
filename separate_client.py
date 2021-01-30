import threading
import re
import info_client
import random
import s_r_mess

ThreadCount = [1,2,3,4]

def modify_conn_info(response, connection, all_client_info):
    global ThreadCount
    random_num = random.choice(ThreadCount)
    ThreadCount.remove(random_num)
    all_client_info.change_list(response,random_num,connection)

class separete_client(threading.Thread):

    def __init__(self, threadID, name, connection, all_client_info):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.connection = connection
        self.response = ""
        self.all_client_info = all_client_info

    def run(self):
        s_r_mess.send_m("CONNECTED\n",self.connection)
        while True:
            self.response = s_r_mess.recv_mess(self.connection)
            regex = re.compile('LOGIN ......')
            match = 'no'
            info = self.all_client_info.get_list()
            resss = self.response
            print(info)
            print("kl")
            for string in info:
                print("KK")
                print(string[0])
                print("")
                print(type(string[0]), type(resss))
                print("")
                if str(resss) == str(string[0]):
                    match = 'yes'
            if re.match(regex, self.response) and match == 'no':
                s_r_mess.send_m("OK\n", self.connection)
                modify_conn_info(self.response.rstrip("\n"), self.connection, self.all_client_info)
                break
            else:
                s_r_mess.send_m("ERROR\n", self.connection) 

    def get_response(self):
        return self.response