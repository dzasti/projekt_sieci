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

while res != "OK":
    Input = input()
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    res = res.decode('utf-8')
    print(res)
############################################## end of login #######################################################
res = ClientMultiSocket.recv(1024)
res = res.decode('utf-8')
print(res)

print("umieram")

ClientMultiSocket.close()
