import socket
import threading
import pickle as pk
from threading import *


class mainServer(threading.Thread):
    def __init__(self, max_connection):
        threading.Thread.__init__(self)
        self.host = 'localhost'
        self.semaphore = Semaphore(max_connection)
        self.port = 3456
        self.serv = socket.socket()
        print("Central server is live")
        self.serv.bind((self.host, self.port))
        self.serv.listen(max_connection)
        self.files = []
        self.keys = ['peer_id', 'file_name']
        #  key list it have only two value peer_id and file name as string  
        # i create it for disply 
        print("Get connected at", self.host, "on port number", self.port)

    def run(self):
        while True:
            client, addr = self.serv.accept()
              #accept it wait for any connection from any client
        #  and it will return a socket representing the connection
        #  and the address of the client
            print("Connected to", addr[0], "Port at", addr[1])
#addr 0 IS the address of localhost 127.0.0.1
#addr 1 is the nbr of port of each peer
            request = pk.loads(client.recv(1024))
            # request to get clients requests using loads function 
            # for de-serialize the binary file  back to the orignal object


            if request[0] == 1:
                print("Peer", addr[1], "Add new file")
                #The semaphore can be acquired by calling the acquire() function
                self.semaphore.acquire()
                self.register(request[1], request[2])
                ret = "File Registered Successfully."
                client.send(bytes(ret, 'utf-8'))
                #bytes translate to binary 
                #the semaphore can be released again by calling the release() function
                self.semaphore.release()
                client.close()
            elif request[0] == 2:
                print("Peer", addr[1], "Searching for a file")
                self.semaphore.acquire()
                ret_data = pk.dumps(self.search_data(request[1]))
                 #  get clients requests using dumps function for serialize  object
                 # translat the name of file from original object to pk object and show it

                client.send(ret_data)
                self.semaphore.release()
                client.close()
            elif request[0] == 3:
                print("Peer", addr[1], "Listing all files")
                self.semaphore.acquire()
                ret_data = pk.dumps(self.all_data())
                # translat the name of  each file from original object to pk object and show them

                client.send(ret_data)
                self.semaphore.release()
                client.close()
            else:
                continue

    def register(self, peer_id, file_name):
        entry = [str(peer_id), file_name]
        self.files.insert(0, dict(zip(self.keys, entry)))

    def search_data(self, file_name):
        found = []
        for item in self.files:
            if item['file_name'] == file_name:
                entry = [item['peer_id'], item['file_name']]
                found.insert(0, dict(zip(self.keys, entry)))
                #insert in the beging of found list 'last in first out'
        return found, self.keys

    def all_data(self):
        return self.files, self.keys


# Main
print("Welcome. Server is about to go live")
server = mainServer(2)
server.start()
