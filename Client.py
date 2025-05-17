import zmq
from datetime import date

#parameters
curDate = date.today()
foodItems = [["Bread", date(2025, 5, 21)],
             ["Milk", date(2025, 5, 15)],
             ["Cheese", date(2025, 5, 18)],
             ["Eggs", date(2025, 5, 7)]]
exprDate = date(2025, 5, 21)

for foodItem in foodItems:
    #Start Microservice
    context = zmq.Context()
    print("Client attempting to connect to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    #create request for server
    request = [foodItem[0].encode(), foodItem[1].strftime("%Y-%m-%d").encode()]

    print(f"Sending a request...")
    socket.send_multipart(request)

    message = socket.recv()
    print(f"Server sent back: {message.decode()}")

print(f"ending microservice")
socket.send_multipart(['Q'.encode(), curDate.strftime("%Y-%m-%d").encode()])

#https://www.google.com/search?q=python+zeromq+sending+request+with+multiple+parameters&sca_esv=c95f54241bee1759&ei=RfInaI_ULY2h0PEPxNeJ2Ak&ved=0ahUKEwjPiqPEuKmNAxWNEDQIHcRrApsQ4dUDCBI&uact=5&oq=python+zeromq+sending+request+with+multiple+parameters&gs_lp=Egxn
