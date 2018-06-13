import socket

try:
    import colorama
except:
    print("Please install colorama to continue")

def __init__():
    colorama.init()

    global host
    global port

    host = "127.0.0.1"    #Replace with hostname
    port = 80   #Replcae with your port to use

    return host
    return port

__init__()

def main():
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(">>>")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print (colorama.Fore.YELLOW + data)
                 
                message = input(">>>")
                 
        mySocket.close()
 
if __name__ == '__main__':
    main()
