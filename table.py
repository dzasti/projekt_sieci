class table():

    def __init__(self, arr):
        self.arr = arr

    def append(self,element):
        self.arr.append(element)
    
    def remove(self):
        del self.arr[0]
    
    def get_1_el(self):
        return self.arr[0]
        
    def get(self):
        return self.arr
    
    def get_len(self):
        return len(self.arr)