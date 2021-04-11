import socket
CHUNK=65535 # max data recieved at once in bytes

port=3000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
"""
create a socket object
socket.socket(family, type)
AF_NET: family of IPv4 IP Adresses
SOCK_DGRAM: UDP, SOCK_STREAM: TCP
"""

# print(s)

"""
somw ip address that the server will listen to when message comes
"""
hostname='127.0.0.1' # ip address of local machine, same for everyone
# aka home, there is no place like 127.0.0.1

s.bind((hostname, port)) 
"""
bind the socket with the host machine on port 3000
"""
print(f"Server is live  on {s.getsockname()}")

"""
run this server infinitely, till it is stopped manually
"""
while True:
	data,clientAdd=s.recvfrom(CHUNK)
	"""
	it is listening infinitely
	whenever someone sends any data on the URL,
	this method will get called
	"""
	message=data.decode('ascii') # since data, by deft, travels in bytes
	# print(f"Person2 at {clientAdd} says: {message}.")
	print(f"Person2: {message}")
	message_send=input("Reply:")
	data=message_send.encode('ascii')
	# send data to the IP add that sent me the data

	s.sendto(data, clientAdd)