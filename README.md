# TCP-client

A simple TCP client I programmed for my networks class in Python. The goal is to interact with the classes server by evaluating these string expressions that would be sent to the client from the server.

These expressions are evaluated by the client and then the result is sent back to the server. In the event that the wrong evaluation is sent to the server, the server terminates with a message stating the client failed to correctly evaluate all the servers expressions.

Once all the expressions are evaluated correctly and received by the server, the server will give a success message with a flag.