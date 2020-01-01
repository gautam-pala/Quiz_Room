import socket
import time
import thread
import sys
import select
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",12345))
ans="w"
def timer():
	global ans
	ans=raw_input("enter your answer A) B) C) D) and press enter\n")
	return ans
	
while True:
	size=client.recv(100)
	
	if size == "no":
		client.close()
		break
	size=int(size)
	client.send("yes")
	data=client.recv(size)
	print(data)
	ans=thread.start_new_thread(timer,())
	ans=str(ans)
	time.sleep(5)	
	client.send(ans)
	resp=client.recv(100)
	print(resp)
	client.send("yes")
'''
output
1)Email uses which protocol?
 A)SMTP
 B)UDP
 C)TCP
 D)NO ONE

enter your answer A) B) C) D) and press enter
A
true marks 1 ans A

2)Types of switching?
 A)packet
 B)circuit
 C)none
 D)A and B both

enter your answer A) B) C) D) and press enter
false marks 1 ans D

3)What is the maximum size of data that the application layer can pass on to the TCP layer below?
 A)any size
 B)2^16 bytes
 C)2^16 bits
 D)none

A
enter your answer A) B) C) D) and press enter
true marks 2 ans A

'''
