#Sentdex

import socket
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 50000))

while True:
	full_msg = b''
	new_msg = True
	while True:
		msg = s.recv(16)
		if len(msg) <= 0:
			break
		if new_msg:
			print(f"new message length: {msg[:HEADERSIZE]}")
			msglen = int(msg[:HEADERSIZE])
			new_msg = False
			
		full_msg  += msg
		
		if len(full_msg) - HEADERSIZE == msglen:
			print("Full message received")
			#print(full_msg[HEADERSIZE:]) 
			d = pickle.loads(full_msg[HEADERSIZE:])
			print(d)
			new_msg = True
			full_msg = ''
		

