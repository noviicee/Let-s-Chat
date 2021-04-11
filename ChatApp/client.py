import socket
port=3000
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket object
CHUNK=65535

"""
instead of explicitly binding the OS
/s.bind((hostname, port)) 
I will let the OS do it, and let the host take care of the IP Addr
"""
#ephemral ports

hostname='127.0.0.1'
while True:
	s.connect((hostname, port)) #connect to server.py
	message=input("Type message:")
	data=message.encode("ascii")
	s.send(data)
	# data recieved
	data=s.recv(CHUNK)
	text=data.decode("ascii")
	print(f"Person1: {text}")