#!/usr/bin/env python3
import socket
import sys
import multiprocessing

# Send Message
def sendTCP(host, port, num, data):
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
        sock.connect((host, port))
        # Send NUM_MESS message
        for _ in range(num) : 
            sock.sendall(data)

# IP address and Port
HOST, PORT = "10.28.8.%s"%(sys.argv[3]), 19091

# Send text data
numbyte = int(sys.argv[2])
data = bytes('A'*numbyte + '\n', "utf-8")

# Send file data
# archfile = open('arch.zip','rb')
# data = archfile.read()

# Number of message
NUM = int(sys.argv[1])

# Multi Process
lstProc  = []
NUM_PROC = 8

for i in range(NUM_PROC) :
    lstProc.append(multiprocessing.Process(target=sendTCP, args=(HOST, PORT, NUM//NUM_PROC, data)))

for i in range(NUM_PROC) :
    lstProc[i].start()
for i in range(NUM_PROC) : 
    lstProc[i].join()

# Single process
# sendTCP(HOST, PORT, NUM, data)
