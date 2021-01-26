import threading
import re
import info_client
import choiceList
import order_

class start_message:

    def __init__(self, order, order3, all_client_info, choice_list, choice_list2):
        self.order = order
        self.order3 = order3
        self.all_client_info = all_client_info
        self.choice_list = choice_list
        self.choice_list2 = choice_list2

    def execute(self):

        ORD = list(self.order.split(" ")) 
        for x in ORD:
            for x2 in self.all_client_info:
                if str(x2[1]) == x:
                    x3 = x2
            x3[2].send(str.encode("YOUR CHOICE\n"))
            while True:
                data = x3[2].recv(1024)
                response = data.decode('utf-8')
                response = response.rstrip("\n")
                regex = re.compile('CHOOSE *')
                match = 'no'
                for string in self.choice_list:
                    if response.replace('CHOOSE ', '') == string:
                        match = 'yes'
                if re.match(regex, response) and match == 'yes':
                    x3[2].send(str.encode("OK\n"))
                    OP = self.choice_list2.index(response.replace('CHOOSE ', ''))
                    self.order3[OP] = x3[1]
                    self.choice_list.remove(response.replace('CHOOSE ', ''))
                    var = str(x3[1])
                    for x4 in self.all_client_info:
                        if str(x4[1]) != str(x3[1]):
                            x4[2].send(str.encode("PLAYER CHOICE " + var + " " + response.replace('CHOOSE ', '') + "\n"))
                    break
                else:
                    x3[2].send(str.encode("ERROR\n"))
    