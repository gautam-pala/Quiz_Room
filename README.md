# Quiz_Room
The Repository contain  
1) client.py  
2) server.py  

Implementation of a Quiz Room using socket programming.   The server program is permit multiple clients to join the quiz room and keep track of the list of clients in the quiz room. It fetch the multiple choice questions in Aiken Format one at a time and send it to all the clients present in the quiz room. Further, it fetch a response from each client and give feedback - answer is correct or incorrect or no response received (communicate correct answer in the later two case) .   The client join the Quiz room and wait for the server to post the question. For every question posted by the server, the client may decide (not) to send response.
