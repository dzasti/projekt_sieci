import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
print(res.decode('utf-8'), end = '')

######################################## LOGGING IN ##########################################

while res != "OK\n":
    Input = input()
    ClientMultiSocket.send(str.encode(Input + "\n"))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = '')

######################################## START ###############################################

res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res, end = "")
res = res.replace('START ', '')
order = [res[2], res[4], res[6] ,res[8]]
wart = 0
check = res[0]
while order[wart] != check:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
    wart = wart + 1
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res, end = "")
while res != "OK\n":
    Input = input()
    ClientMultiSocket.send(str.encode(Input + "\n"))
    #print(Input + "\n", end = "")
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
while wart != 3:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
    wart = wart + 1

####################################### ROUNDS ################################################

res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
res = res.rstrip("\n")
order = list(res.split(" "))
print(order)
print(order[:6])
order = order[5:9]
res = res[:5]
#print(res)
print(order)
wart = 0
while order[wart] != check:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
    wart = wart + 1
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res,end = "")
while res != "OK\n":
    Input = input()
    ClientMultiSocket.send(str.encode(Input + "\n"))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res,end = "")
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res,end = "")
while res != "OK\n":
    Input = input()
    ClientMultiSocket.send(str.encode(Input + "\n"))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res, end = "")
while wart != 3:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res,end = "")
    wart = wart + 1

ClientMultiSocket.close()
