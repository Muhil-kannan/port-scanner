#!/bin/python

import sys
import socket
from datetime import datetime

#Defining Our Target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translating hostname to IPV4
else:
    print("Invalid Amount Of Arugument Dude.")
    print("synatx:python3 scanner.py <ip>")

#banner
print("-" * 50)
print("Scanning Target"+target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except keyboardInterrupt:
    print("\n Exiting Program.")
    sys.exit()

except socket.gaierror:
    print("Host Name Could Not Be Resolved.")
    sys.exit

except socket.error:
    print("could not connect to server.")
    sys.exit


    #Muhilkannan - muhil0304@gmail.com
