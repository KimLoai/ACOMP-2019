#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time
import datetime
import os

# Send Message
def sendMQTT(host, port, num, data, topic):
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)
    for i in range(num) : 
        client.publish(topic , data)
    client.disconnect()

# Writing log
def writingLog(startTime, execTime, message):
    # Create log dictionary
    if (not os.path.exists("log/")):
        os.mkdir("log/")
    # Log file    
    today = datetime.date.today()
    currDate = today.strftime("%d-%m-%Y")
    path = "log/" + "mqtt" + currDate + ".log"
    outputFile = open(path, 'a+')
    
    # Write log
    outputFile.write("%s\t%13d\t%15.6f\n" %(startTime, message, execTime))

###################### CONSTANTS ########################

# IP address and Port
HOST, PORT = "10.28.8.86", 1883
# Topic name
topic = "nifi"
# Date send
data = 'a'
# Num message
num_message = [1000*(2**i) for i in range(7)]

####################### MAIN ###########################

for message in num_message:
    start = time.time()
    startTime = datetime.datetime.now().time()
    sendMQTT(HOST, PORT, message, data, topic)
    end = time.time()
    execTime = end - start
    writingLog(startTime, execTime, message)
