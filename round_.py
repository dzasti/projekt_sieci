import re

cordinate = list(range(-100,101))
orientation = [0,90,180,270]

class round_:

    def __init__(self, order, order3, all_client_info, choice_list, choice_list2):
        self.order = order
        self.order3 = order3
        self.all_client_info = all_client_info
        self.choice_list = choice_list
        self.choice_list2 = choice_list2

    def execute_(self):

        ORD = self.order
        #self.order3 = list(self.order3.split(" "))
        print(ORD)
        for x in ORD:
            for x2 in self.all_client_info:
                if str(x2[1]) == x:
                    x3 = x2
            x3[2].send(str.encode("YOUR MOVE\n"))
            while True:
                data = x3[2].recv(1024)
                response = data.decode('utf-8')
                response = response.rstrip("\n")
                regex = re.compile('MOVE *')
                match = 'no'
                print("odebralo komunikat")
                helpList = list(response.split(" "))
                m1 = 0
                #m2 = 0
                if len(helpList) == 4 and re.match(regex, response) and (int(helpList[1]) in cordinate) and (int(helpList[2]) in cordinate) and (int(helpList[3]) in orientation):
                    m1 = 1
                if(m1 == 1):
                    print("weszlo do petli")
                    x3[2].send(str.encode("OK\n"))
                    for x4 in self.all_client_info:
                        if x4 != x3:
                            x4[2].send(str.encode("PLAYER MOVE " + helpList[1] + " " + helpList[2] + " " + helpList[3] + "\n"))
                    break
                else:
                    x3[2].send(str.encode("ERROR\n"))
    
            x3[2].send(str.encode("YOUR CHOICE\n"))
            while True:
                data = x3[2].recv(1024)
                response = data.decode('utf-8')
                response = response.rstrip("\n")
                regex = re.compile('CHOOSE *')
                match = 'no'
                print("odebralo komunikat")
                for string in self.choice_list:
                    if response.replace('CHOOSE ', '') == string:
                        match = 'yes'
                        print("znalazlo element")
                if re.match(regex, response) and match == 'yes':
                    print("weszlo do petli")
                    x3[2].send(str.encode("OK\n"))
                    OP = self.choice_list2.index(response.replace('CHOOSE ', ''))
                    self.order3[OP] = x3[1]
                    self.choice_list.remove(response.replace('CHOOSE ', ''))
                    for x4 in self.all_client_info:
                        if x4 != x3:
                            x4[2].send(str.encode("PLAYER CHOICE " + str(x3[1]) + " " + response.replace('CHOOSE ', '') + "\n"))
                    break
                else:
                    x3[2].send(str.encode("ERROR\n"))

                    