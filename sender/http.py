import requests
import datetime
import os
import time

# Send Message
def sendHTTP(url, num, data):
    for i in range(num) : 
        response = requests.post(url, data=data)

# Writing log
def writingLog(startTime, execTime, message):
    # Create log dictionary
    if (not os.path.exists("log/")):
        os.mkdir("log/")
    # Log file    
    today = datetime.date.today()
    currDate = today.strftime("%d-%m-%Y")
    path = "log/" + "http" + currDate + ".log"
    outputFile = open(path, 'a+')
    
    # Write log
    outputFile.write("%s\t%13d\t%15.6f\n" %(startTime, message, execTime))

###################### CONSTANTS ########################

# Address of HTTP Listener
url = 'http://10.28.8.86:19090/httplistener'

# Send text data
data = 'a'

# Num message
num_message = [1000*(2**i) for i in range(7)]

####################### MAIN ###########################

for message in num_message:
    start = time.time()
    startTime = datetime.datetime.now().time()
    sendHTTP(url, message, data)
    end = time.time()
    execTime = end - start
    writingLog(startTime, execTime, message)
