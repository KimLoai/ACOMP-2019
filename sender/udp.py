#!/usr/bin/env python3
import time
import socket
import datetime
import os
import sys
import multiprocessing
# Send Message
def sendUDP(host, port, num, data):
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Connect to server and send data
        sock.connect((host, port))
        # Send NUM_MESS message
        for _ in range(num) : 
            sock.sendall(data)

# IP address and Port
HOST, PORT = "10.28.8.%s"%(sys.argv[3]), 19092

# Send text data
numbyte = int(sys.argv[2])
data = bytes('A'*numbyte, "utf-8")


# Number of message
NUM = int(sys.argv[1])

# Multiple process
lstProc  = []
NUM_PROC = 8

for i in range(NUM_PROC) :
    lstProc.append(multiprocessing.Process(target=sendUDP, args=(HOST, PORT, NUM, data)))

for i in range(NUM_PROC) :
    lstProc[i].start()
for i in range(NUM_PROC) : 
    lstProc[i].join()

# # Single process
# sendUDP(HOST, PORT, NUM, data)
