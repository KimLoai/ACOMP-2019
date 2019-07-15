import sys
import multiprocessing
import paho.mqtt.client as mqtt

# Send Message
def sendMQTT(host, port, num, data, topic):
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)
    for _ in range(num) : 
        client.publish(topic , data)
    client.disconnect()

# IP address and Port
HOST, PORT = "10.28.8.86", 1883
# Topic name
topic = "nifi"
# Number of messages
NUM = int(sys.argv[1])
# Date send
numbyte = int(sys.argv[2])
data = bytes('A\n'*numbyte, "utf-8")

# Multiple process
lstProc  = []
NUM_PROC = 8
NUM = NUM//NUM_PROC

for i in range(NUM_PROC) :
    lstProc.append(multiprocessing.Process(
        target=sendMQTT, 
        args=(HOST, PORT, NUM, data, topic))
    )

for i in range(NUM_PROC) :
    lstProc[i].start()
for i in range(NUM_PROC) : 
    lstProc[i].join()

# Single Process
# sendMQTT(HOST, PORT, NUM, data, topic)
