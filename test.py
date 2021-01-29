# Online Python compiler (interpreter) to run Python online.
VALUE = 200
a = [[0 for i in range(VALUE)] for j in range(VALUE)]
a[2][2] = "ten z ktorym trzeba trzymac"
a[2][3] = "ten z ktorym trzeba trzymac"
a[0][0] = "zajete"
b = ["s s","s s","f f","f f","f f","f f","w w","w w","w w","g g","g g","b b","s f","s w","s g","s b","f w","f g","s1 f","s1 w","s1 g","s1 b","s1 m","f1 s","f1 s","f1 s","f1 s","f1 w","f1 g","w1 s","w1 s","w1 f","w1 f","w1 f","w1 f","s g1","w g1","s b1","g b1","m1 s","s g2","w g2","s b2","g b2","m2 s","b m2","b m2","s m3"]
mess = input("wprowadz: ")

"""
def manage_mess(mess,line,column):
mess = list(mess.split(" "))
element = int(mess[0]) - 1
line = int(mess[1]) - 1
column = int(mess[2]) - 1
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
"""

def is_aproved(line,column,a,b,VALUE):

    neigh = [[line,column+1],[line-1,column],[line,column-1],[line+1,column]]
    wart = 0
    print(line,column,VALUE)

    for x in neigh:
        if(0<=x[0]<=VALUE-1 and 0<=x[1]<=VALUE-1):
            if(a[x[0]][x[1]]!=0):
                wart = 1

    if(wart==0):
        return False
    else:
        return True                
            
def manage_board(a,b,line,colum,mess,VALUE):
########
    mess = list(mess.split(" "))
    element = int(mess[0]) - 1
    line = int(mess[1]) - 1
    column = int(mess[2]) - 1
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
#########
    if (a[line][column] == 0 and a[line2][column2] == 0):
        if(is_aproved(line,column,a,b,VALUE) or is_aproved(line2,column2,a,b,VALUE)):
            to_insert = b[element]
            to_insert = list(to_insert.split(" "))
            return to_insert
        else:
            return False
    else:
        return False
