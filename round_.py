import re
import boards


cordinate = list(range(-100,101))
orientation = [0,90,180,270]
ble = 0

def checking(tablica):
    print("tutaj sprawdzanie które są zajęte")
    for x in tablica:
        for y in x:
            if (y != 0):
                print(tablica.index(x),x.index(y))

def get_from_char(element,characters):

    print("szukankko")
    print(element, type(element))
    print(characters, type(characters))
    for x in characters:
        if characters.index(x) == int(element):
            print("znalazlo")
            return x

def get_from_char2(element,characters):

    print("szukankko")
    print(element, type(element))
    print(characters, type(characters))
    for x in characters:
        if characters.index(x) == element:
            print("zanlazlo")
            return x

def search_board(index,board):

    if index == 1 :
        print("tak weszlozzzz")
        return board.get_a()
    elif index == 2 :
        print("tak weszlozzzz")
        return board.get_b()
    elif index == 3 :
        print("tak weszlozzzz")
        return board.get_c()
    elif index == 4 :
        print("tak weszlozzzz")
        return board.get_d()

def manage_mess(mess):   
    line = int(mess[1]) + 100
    column = int(mess[2]) + 100
    line2 = line
    column2 = column
    if int(mess[3]) == 0:
        column2 = column + 1
    if int(mess[3]) == 90:
        line2 = line + 1
    if int(mess[3]) == 180:
        column2 = column - 1
    if int(mess[3]) == 270:
        line2 = line - 1
    return [line,column,line2,column2]

def is_next_to_neigh(line,column,a):

    neigh = [[line,column+1],[line-1,column],[line,column-1],[line+1,column]]
    wart = 0

    print(neigh, type(neigh))
    print(line, type(line))
    print(column, type(column))
    #print(a, type(a))

    for x in neigh:
        if(0<=x[0]<=200 and 0<=x[1]<=200):
            print("dobry przedzial")
            if(a[x[0]][x[1]]!=0):
                print(a[x[0]][x[1]], type(a[x[0]][x[1]]))
                wart = 1
    if(wart==0):
        return False
    else:
        return True   

def is_approved(a,line,column,line2,column2):

    print("tutaj są lokalizacje obu pointow")
    print(line, column)
    print(line2, column2)

    if (a[line][column] == 0 and a[line2][column2] == 0):
        if(is_next_to_neigh(line,column,a) or is_next_to_neigh(line2,column2,a)):
            return True
        else:
            return False
    else:
        return False

def insert_to_board(board,element,line,column,line2,column2):
    
    element = list(element.split(" "))
    board[line][column] = element[0]
    board[line2][column2] = element[1]

class round_:
    
    ble = 0

    def __init__(self, order, order3, all_client_info, choice_list, choice_list2,board):
        self.order = order
        self.order3 = order3
        self.all_client_info = all_client_info
        self.choice_list = choice_list
        self.choice_list2 = choice_list2
        self.board = board

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
                m2 = 0
                print(helpList)
                print(len(helpList))
                print(re.match(regex, response))
                if(len(helpList) == 4 and re.match(regex, response)):
                    print("1")
                    try:
                        int(helpList[1])
                        int(helpList[2])
                        int(helpList[3])
                    except:
                        return
                    #if(helpList[1].isdigit()) and (helpList[2].isdigit()) and (helpList[3].isdigit()):
                    print("2")
                    if(int(helpList[1]) in cordinate) and (int(helpList[2]) in cordinate) and (int(helpList[3]) in orientation):
                        print("3")
                        m1 = 1
                        modified_mess = manage_mess(helpList)
                        curr_board = search_board(x3[1],self.board)
                        print("jeden")
                        m2 = is_approved(curr_board,modified_mess[0],modified_mess[1],modified_mess[2],modified_mess[3])
                        #checking(curr_board)
                if(m1 == 1 and m2):
                    print("weszlo do petli")
                    x3[2].send(str.encode("OK\n"))
                    el_from_characters = self.board.get_el_by_index(x3[3])
                    print(el_from_characters)
                    insert_to_board(curr_board,el_from_characters,modified_mess[0],modified_mess[1],modified_mess[2],modified_mess[3])
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
                    index = self.all_client_info.index(x3)
                    self.all_client_info[index][3] = response.replace('CHOOSE ', '')
                    for x4 in self.all_client_info:
                        if x4 != x3:
                            x4[2].send(str.encode("PLAYER CHOICE " + str(x3[1]) + " " + response.replace('CHOOSE ', '') + "\n"))
                    break
                else:
                    x3[2].send(str.encode("ERROR\n"))
        print(self.all_client_info)
        self.ble = self.ble + 1
            

                    