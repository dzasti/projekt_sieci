

class info_client:
    def __init__(self, ind_list):
        self.ind_list = ind_list

    def get_list(self):
        return self.ind_list 

    def change_list(self, response, random_num, connection):
        self.ind_list.append([response,random_num,connection,"0"])
    
    def append_curr_number(self, index, element):
        self.ind_list[index].append(element)