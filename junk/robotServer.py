import socket

class RobotServer(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
    
    def run(self):
        #TESTAR MED SOCKET HÄR
        s = self.socket
    	#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
         #   s.bind((self.host, self.port))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
#SLUTAR TESTA MED SOCKET HÄR