##########################################

## Description: The program here first creates the client socket, and connects with the server.
## Then, the python program sends an initial message with ID, then if the server accepts it, 
## the server returns a message of evaluations.
## Then the program enters the while loop, which continues until the server message returns a failure message, 
## a success message with a flag id, or invalid type message.
## If neither of these things happen, the client calculates the expression, 
## and sends the result to the server, and it continues in the while loop.
## The client socket then closes at the end.

##########################################

# imports
from socket import *

# constant variables
server_address = "" #Class server is shut down now
server_portnumber = 12000
buffer_size = 4096
identifier = (server_address , server_portnumber)
iterator = True
num_eval = 0

# function that evaluates expression
def eval(v1, expr, v2):
    if(expr == "+"):
        return int(v1) + int(v2)
    elif(expr == "-"):
        return int(v1) - int(v2)
    elif(expr == "*"):
        return int(v1) * int(v2)
    elif(expr == "/"):
        return int(v1) / int(v2)
    else:
        print("Expression error")

# initialize the socket
client_socket = socket(AF_INET , SOCK_STREAM)
client_socket.connect(identifier)

# initial message to server
introductory = "EECE2540 INTR ID#"
client_socket.send(introductory.encode('utf-8'))
print("Introductory message sent")

# continues to evaluate expressions, exit when either fail or successful or invalid
while(iterator):

    # get message from server
    message_from_server = client_socket.recv(buffer_size)
    message = message_from_server.decode()
    mess = message.split()
    
    # if expression received
    if mess[0] == "EECE2540" and mess[1] == "EXPR":
        result = eval(mess[2], mess[3], mess[4])
        sent = "EECE2540 RSLT " + str(result)
        client_socket.send(sent.encode('utf-8'))
        num_eval += 1
    # if failure received
    elif mess[0] == "EECE2540" and mess[1] == "FAIL":
        iterator = False
        print("Number of evaluations: " + str(num_eval))
        print("Expression Evaluation Failed")
    # if success received
    elif mess[0] == "EECE2540" and mess[1] == "SUCC":
        iterator = False
        print("Number of evaluations: " + str(num_eval))
        print("Secret flag: " + str(mess[2]))
    # if invalid message type received
    else:
        iterator = False
        print("Number of evaluations: " + str(num_eval))
        print("Invalid message format")

client_socket.close()