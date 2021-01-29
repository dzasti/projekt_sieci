
class boards:

    VALUE = int(200)
    a = []
    b = []
    c = []
    d = []
    characters = ["0 0","s s","s s","f f","f f","f f","f f","w w","w w","w w","g g","g g","b b","s f","s w","s g","s b","f w","f g","s1 f","s1 w","s1 g","s1 b","s1 m","f1 s","f1 s","f1 s","f1 s","f1 w","f1 g","w1 s","w1 s","w1 f","w1 f","w1 f","w1 f","s g1","w g1","s b1","g b1","m1 s","s g2","w g2","s b2","g b2","m2 s","b m2","b m2","s m3"]

    def manage_boards(self):
        self.a = [[0 for i in range(self.VALUE)] for j in range(self.VALUE)]
        self.b = [[0 for i in range(self.VALUE)] for j in range(self.VALUE)]
        self.c = [[0 for i in range(self.VALUE)] for j in range(self.VALUE)]
        self.d = [[0 for i in range(self.VALUE)] for j in range(self.VALUE)]
        self.a[100][100] = "a a"
        self.b[100][100] = "a a"
        self.c[100][100] = "a a"
        self.d[100][100] = "a a"
    
    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c
    
    def get_d(self):
        return self.d

    def get_characters(self):
        return self.characters

    def get_el_by_index(self,index):
        index2 = int(index)
        return self.characters[index2]
    
    
    
