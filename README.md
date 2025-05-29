# Microservice-A
Repository for my microservices for Bernard Laughlin
Contains program for microservice A (ExpirationDateServer.py) And a program to test it (ExpirationDateClient.py)

You can contact me through Discord. My account is joseph11112496.

## How to REQUEST Data:

  The server requires a multipart request. That means you need to make an array with atleast two items. The first should be a food item, and the second the expiration date of the food item.
## example request:
  request = [foodItem.encode(), expirationDate.strftime("%Y-%m-%d").encode()]
  socket.send_multipart(request)

## How to RECEIVE Data:

  The server sends back a string saying" "{food_item} is {reply}". Reply becomes expired if the expiration date is passed the current date, and not expired otherwise.
## example receive
  message = socket.recv()

  How to Quit:
    send a multipart request where either the first or second item is 'Q'. That will stop the server.
![UML Sequence Diagram.pdf](https://github.com/user-attachments/files/20266538/UML.Sequence.Diagram.pdf)



