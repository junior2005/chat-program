import socket

try:
    import colorama
except:
    print("Please install colorama to continue")
    exit()

def __init__():
    colorama.init()
    
    global host
    global port

    port = 80
    host = "127.0.0.1"

    return host
    return port

__init__()

def main():
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print (colorama.Fore.GREEN + "Connection from: " + str(addr))
    colorama.Fore.YELLOW
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print (colorama.Fore.YELLOW + str(data))
            conn.send(data.encode())             
    conn.close()
     
if __name__ == '__main__':
    main()
