#Required module to send messages
import socket
import glob

#If colorama is not installed the program will exit
try:
	import colorama
	from colorama import init
except:
	print("Colorama not installed")
	print("Please install to continue")
	exit()

def __init__():
	init()

	#Makes variables "port" and "host" global variables
	global port
	global host
	
	port = 8010		#Port used to send messages through
					#This port must have port forwarding turned on
	
	host = "192.168.0.53"	#Hosts ip address
	
	return host
	return port

__init__()



