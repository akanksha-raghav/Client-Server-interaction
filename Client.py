import socket  #module
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(("127.0.0.1",5000))
s.listen(5)
conn,addr=s.accept()
print("You got connected from address",addr)
while True:
	a="Akanksha==>"+input("")
	conn.send(bytes(a,encoding='utf-8'))
	print(conn.recv(1024))
	
