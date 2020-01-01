import sys
import thread
import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",12345))
server.listen(5)
l=[]

def read(c,file1):
	status=True
	r1=file1.readline()
	ans=0
	if r1.strip() == "bye":
		print("file finished")
		status=False
		return r1,ans,status

	while r1[-2] !='?':
		g1=file1.readline()
		g1.strip()
		r1=r1+" "+g1
	for i in range(0,4):
		r1=r1+" "+file1.readline()
	ans=file1.readline()
	return r1,ans,status
	
def client(c,addr):
	mark=0
	file1=open("demo.txt","r")
	while True:
		d,a,status=read(c,file1)
		if status==True:	
			size=str(sys.getsizeof(d))
			c.send(size)
			c.recv(100)
			c.send(d)
			ansclient=c.recv(100)
			if ansclient.strip() == a.strip():
				mark+=1
				z=str(mark)
				c.send("true marks "+z+" ans "+a)
				c.recv(100)
			else:
				z=str(mark)
				c.send("false marks "+z+" ans "+a)
				c.recv(100)
		else:		
			c.send("no")	
			print("send no")
			l.remove(c)
			break

while True:
	c,addr=server.accept()
	l.append(c)
	thread.start_new_thread(client,(c,addr))

'''
output
file finished
send no
'''
