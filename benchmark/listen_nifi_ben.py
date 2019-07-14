import subprocess
import json
import sys  
import os

# Command to download status history log file of nifi processoir
IP_NIFI   = '10.28.8.%s'%(sys.argv[1]) # IP of Nifi cluster
PORT_NIFI = '8080'       # Port of Nifi cluster
ID_PROC   = sys.argv[2]  # ID of Processor in NIFI
cmd = "curl '%s:%s/nifi-api/flow/processors/%s/status/history'" \
	%(IP_NIFI, PORT_NIFI, ID_PROC) 

messageList = list()
averageMgsPerSec = -100
# Get content of history status log file and store in JSON variable
contents = subprocess.check_output(cmd, shell=True)
jsonFile = json.loads(contents)['statusHistory']['aggregateSnapshots']

for indexJson in range(1, len(jsonFile) - 1):
    if jsonFile[indexJson]['statusMetrics']['Messages Received'] <= 1:
        continue
    curr_mess_count = jsonFile[indexJson + 1]['statusMetrics']['Messages Received']
    prev_mess_count = jsonFile[indexJson]['statusMetrics']['Messages Received']
    mess_recv_pmin  = curr_mess_count - prev_mess_count
    # if curr_mess_count <= prev_mess_count:
    #     break
    if mess_recv_pmin > 0:
        messageList.append(mess_recv_pmin)

if len(messageList) != 0:
    averageMgsPerSec = sum(messageList[:-2]) / len(messageList[:-2])

if (not os.path.exists("./log/")):
    os.mkdir("./log/")
with open("./log/" + ID_PROC + ".csv", 'w+') as outputFile:
    outputFile.writelines('\n'.join(list(map(str, messageList[:-2]))))
    print('\n'.join(list(map(str, messageList[:-2]))))
    outputFile.write("\nMessages per second: " + str(averageMgsPerSec) + " Mgs/s")
    print("\nMessages per second: " + str(averageMgsPerSec) + " Mgs/s")
