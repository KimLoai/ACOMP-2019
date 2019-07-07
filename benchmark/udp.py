#!/usr/bin/env python3
import time
import socket
import datetime
import os
import sys

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
HOST, PORT = "10.28.8.70", 19092

# Send text data
data = bytes('A', "utf-8")

# Number of message
NUM = int(sys.argv[1])

# Single process
sendUDP(HOST, PORT, NUM, data)
