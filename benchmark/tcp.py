#!/usr/bin/env python3
import time
import socket
import datetime
import os

# Send Message
def sendTCP(host, port, num, data):
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
        sock.connect((host, port))
        # Send NUM_MESS message
        for i in range(num) : 
            sock.sendall(data)

# Writing log
def writingLog(startTime, execTime, message):
    # Create log dictionary
    if (not os.path.exists("log/")):
        os.mkdir("log/")
    # Log file    
    today = datetime.date.today()
    currDate = today.strftime("%d-%m-%Y")
    path = "log/" + "tcp" + currDate + ".log"
    outputFile = open(path, 'a+')
    
    # Write log
    outputFile.write("%s\t%13d\t%15.6f\n" %(startTime, message, execTime))

###################### CONSTANTS ########################

# IP address and Port
HOST, PORT = "10.28.8.86", 19091

# Send text data
data = bytes('a', "utf-8")

# Num message
num_message = [1000*(2**i) for i in range(7)]

####################### MAIN ###########################

num_message = [1000*(2**i) for i in range(7)]

for message in num_message:
    start = time.time()
    startTime = datetime.datetime.now().time()
    sendTCP(HOST, PORT, message, data)
    end = time.time()
    execTime = end - start
    writingLog(startTime, execTime, message)
