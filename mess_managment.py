import threading 
FORMAT = "utf-8"

class gettig_mess(threading.Thread):

    def __init__(self, threadID,name, connection,table):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.connection = connection
        self.table = table

    def run(self):
        try:
            data = self.connection.recv(250).decode(FORMAT)
            while data:
                x = list(data.split("\n"))
                del x[-1]
                for a in x:
                    self.table.append(a)
                data = self.connection.recv(250).decode(FORMAT)
        except IOError as e:
            print(e)
        finally:
            self.connection.close()