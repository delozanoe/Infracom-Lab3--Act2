import socketserver, threading, socket

class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        current_thread = threading.current_thread()
        #The response to what ?
        response = bytes("{}: {}".format(current_thread.name, data), 'ascii')
        print("{}: client: {}, wrote: {}".format(current_thread.name, self.client_address, data))
        #socket.sendto(data.upper(), self.client_address)
        self.request.sendall(response)

class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))

if __name__ == "__main__":
    HOST, PORT = "localhost", 0

    string_input  = input(str('Cuantos clientes va a recibir el men'))
    clients_number = int(string_input)
    #Start a thread woth the server -- that thread will then start one

    server = ThreadedUDPServer((HOST, PORT), ThreadedUDPRequestHandler)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True

    try:
        server_thread.start()
        print("Server started at {} port {}".format(HOST, PORT))
        print("Server loop running in thread:", server_thread.name)
        while clients_number > 0:
            client(HOST, PORT, "We are gonna send the file")
            clients_number -= 1
        server.shutdown()
        #Aca debemos manerar los port
    except (KeyboardInterrupt, SystemExit):
        server.shutdown()
        server.server_close()
        exit()