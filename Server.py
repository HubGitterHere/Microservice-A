import zmq
from datetime import date
from datetime import datetime
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

curDate = datetime.now()
exprDate = datetime.now()
while True:
    message = socket.recv_multipart()
    print(f"Checking if ", message[0], " is expired")
    food_item = message[0].decode()
    exprDateStr = message[1].decode()
    exprDate = datetime.strptime(exprDateStr, "%Y-%m-%d")
    
    if len(message) > 0:
        if message[0].decode()=='Q' or message[1] == 'Q':
            break
        reply = "not expired"
        if exprDate < curDate:
            reply = "expired"
            
        socket.send_string(f"{message[0].decode()} is {reply}")
        
context.destroy()
    #if len(exprDate) > 0:
        #if exprDate.decode()=='Q':
        #    break
        
        
        #reply = f"Reply to {exprDate.decode()}".encode()
        #curDateStr = curDate.strftime("%Y-%m-%d")
        #socket.send_string(curDateStr)
        #socket.send_multipart([food_item, b"", reply])


#use py -m pip instead of pip
#install ZeroMQ with pip install pyzmq
#https://www.google.com/search?q=python+encode+date+to+string+and+back&sca_esv=e34318f18f884edb&ei=mswnaJewN5HN0PEPu_e06Ac&ved=0ahUKEwiX5ZrOlKmNAxWRJjQIHbs7DX0Q4dUDCBI&uact=5&oq=python+encode+date+to+string+and+back&gs_lp=Egxnd3Mtd2l6LXNlcnAiJXB5dGhvbiBlbmNvZGUgZGF0ZSB0byBzdHJpbmcgYW5kIGJhY2syBhAAGBYYHjIIEAAYgAQYogQyBRAAGO8FMgUQABjvBUjGHFC_BliuG3ABeAGQAQCYAWqgAbkMqgEEMTguMbgBA8gBAPgBAZgCFKAC7gzCAgoQABiwAxjWBBhHwgIIEAAYogQYiQXCAgUQIRigAcICBRAhGJ8FmAMAiAYBkAYIkgcEMTguMqAHi5QBsgcEMTcuMrgH6gw&sclient=gws-wiz-serp