class order_:
    
    def __init__(self, orrd):
        self.orrd = orrd

    def change_element(self, index, element):
        self.orrd[index] = element
    
    def get(self):
        return self.orrd

    def change_to_string(self):
        self.orrd = map(str, self.orrd)
        self.orrd = ' '.join(self.orrd)
    
    def change_to_string2(self):
        self.orrd = [str(i) for i in self.orrd]