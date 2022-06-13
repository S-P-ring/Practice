import socket
import threading


class ServerThread(threading.Thread):
    def __init__(self, ip, port, clientsock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsock = clientsock
        print('Create a new thread')


    def run(self):
        print(f'comection from {self.ip=} {self.port=}')
        while True:
            data = clientsock.recv(2048)
            if data.decode('utf-8') == 'close':
                break
            else:
                n1, n2 = data.decode('utf-8').split(' ')
                n1 = int(n1)
                n2 = int(n2)
                sum = n1 + n2
                clientsock.send(bytes(sum))




server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0', 8000))
threads = []


while True:
    server.listen(5)
    (clientsock, (ip, port)) = server.accept()
    thread = ServerThread(ip, port, clientsock)
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()
