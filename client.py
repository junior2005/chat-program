import socket
import sys

try:
    import colorama
except:
    print("Please install colorama to continue")
    exit()

def __init__():
    colorama.init()

    global host
    global port

    port = 80   #Replcae with your port to use
    try:
        host = sys.argv[1]
        host = str(host)
    except:
        print("Host argument not given")
        exit()

    return host
    return port

__init__()

def main():
        colorama.Fore.RED
        mySocket = socket.socket()
        mySocket.connect((host,port))
        message = input(">>>")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print (colorama.Fore.RED + data)
                 
                message = input(">>>")
                 
        mySocket.close()
 
if __name__ == '__main__':
    main()

colorama.deinit()