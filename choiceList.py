class choiceList:

    def __init__(self):
        self.ch_list = []
    
    def get_list(self):
        return self.ch_list 

    def change_list(self, number):
        self.ch_list.append(number)

    def sort_(self):
        self.ch_list.sort()

    def change_to_string(self):
        self.ch_list = map(str, self.ch_list)
        self.ch_list = ' '.join(self.ch_list)
    
    def change_to_list(self):
        self.ch_list = list(self.ch_list.split(" "))

    def change_to_strlist(self):
        self.ch_list = list(map(str, self.ch_list))

    def remove(self, element):
        self.ch_list.remove(element)