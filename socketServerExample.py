import socket
import time
import pickle

d = {1 : "Hey", 2 : "There"}
msg = pickle.dumps(d)
print(msg)

'''
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 50000))
print("host:",socket.gethostname())
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conncetion from {address} has been established!")
	msg = 'welcome to the server!'
	msg = f'{len(msg):<{HEADERSIZE}}' + msg
	clientsocket.send(bytes(msg, "utf-8"))
	
	while True:
		time.sleep(3)
		msg = "the time is " + str(time.time())
		msg = f'{len(msg):<{HEADERSIZE}}' + msg
		clientsocket.send(bytes(msg, "utf-8"))
'''

