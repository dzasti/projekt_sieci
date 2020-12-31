import socket

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
print(res.decode('utf-8'))

######################################## LOGGING IN ##########################################

while res != "OK":
    Input = input()
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)

######################################## START ###############################################

res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res)
res = res.replace('START ', '')
order = [res[2], res[4], res[6] ,res[8]]
wart = 0
check = res[0]
while order[wart] != check:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
    wart = wart + 1
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res)
while res != "OK":
    Input = input()
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
while wart != 3:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
    wart = wart + 1

####################################### ROUNDS ################################################

res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
order = list(res.split(" "))
order = order[5:]
res = res[:-8]
print(res)
print(order)
wart = 0
while order[wart] != check:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
    wart = wart + 1
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res)
while res != "OK":
    Input = input()
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res)
while res != "OK":
    Input = input()
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
while wart != 3:
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
    wart = wart + 1

ClientMultiSocket.close()
