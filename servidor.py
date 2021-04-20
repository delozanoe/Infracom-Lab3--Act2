import socket, hashlib, threading, time, datetime, osas 

#TODO
lock = threading.Lock()
#GLOBAL VARIABLES

attend = 0
BUFFER = 4096


#Varaibles to tranfer
host = ""
BUFFER = 4096



#Menu
def menu():
    fileName = ""
    fileToTransfer = ""
    dataInput = int(input("Select file to send 1 (100 MB) o 2 (250MB"))
    if(dataInput == 1):
        fileName = ""
        fileToTransfer = ".zip"
    elif(dataInput == 2):
        fileName = "
        fileToTransfer =".zip"
    entr = int(input("How many clients do you want to manage: "))
    clientsNumb  = entr
    return fileName, fileToTransfer, clientsNumb

#Data to transfer
file_data = menu()
fileName = file_data[0]
fileToTransfer = file_data[1]
number_clients = file_data[2]
connected_customers = 0
attend = False


#Method Server
def server(port1,dir):
    port = 20001+port1
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    #Bind to addresss and ip
    s.bind((host, port))
    s.sendto(str(port).encode(),dir)

    #Start server
    while True: 
        data = s.recvfrom()
        message  = data[0]
        dir = data[1]

        print("Server received", message.decode())

        if(message.decode() == "LISTENING!):
            connected_customers += 1
            print("Customers connected: ", connected_customers)
            encrypHash = hashlib.sha1()

            while True:
                if(connected_customers >= number_clients or attend ):
                    print("Starting to send")
                    break
            #The server is on and listening
            attend =  True
            i = 0
            s.sendto(fileToTransfer.encode(),dir)

            time.sleep(0.01)

            startTransfer  = time.time()
            #File to transfer
            f = open(fileName, 'rb') 
            while True: 
                i+= 1 
                data = f.read(BUFFER)
                if not data: 
                    break
                encrypHash.update(data)
                s.sendto(data,dir)
            print("Send File")

            #Create Hash 
            hass =  str(encrypHash.hexdigest())
            s.sendto(("FINM"+has).encode(),dir)
            f.close()

            data = s.recvfrom(BUFFER)

            #Notification of recive
            datosCliente  = data[0].decode().split("/")
            reception = datosCliente[1]
            print(reception)

            #Time notification
            endToTransfer = float(datosCliente[2])
            totalTransfer = endToTransfer -startTransfer

            #How many packages has the client recive
            packClientRecive = datosCliente[0]
            hasofRecive = datosCliente[4]

            #LLAMAR METODO DE CLIENTE

            print('End sending')
            connected_customers -=1
            print("Customers connected: ", connected_customers)

            #End or not notification
            endSesion = datosCliente[3]

            if(endSesion == "FINISH"):
                print(endSesion)
                s.close()
                print("End server on port", port)
                break


port_1 = 20001
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
s.bind((host, port_1))
i=1
while True:
    data = s.recvfrom(BUFFER)
    msg = data[0]
    dir = data[1]

    if (msg.decode() == "REQUEST"):
        if(i==26):
            i=1
        t = threading.Thread(target=servidor, args=(i,dir))
        i += 1
        t.start()

    if (msg.decode() == "END"):
        print("FIN CONEXIONES")
        break








    
    
