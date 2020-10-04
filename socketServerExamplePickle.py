#Sentdex

import socket
import time
import pickle




HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 50000))
print("host:",socket.gethostname())
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conncetion from {address} has been established!")
	d = {1 : "Hey", 2 : "There"}
	msg = pickle.dumps(d)
	print(msg)
	msg = bytes(f'{len(msg):<{HEADERSIZE}}',"utf-8") + msg
	clientsocket.send(msg)


