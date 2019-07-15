import subprocess
import json
import sys

# Command to download status history log file of nifi processoir
IP_NIFI   = '10.28.8.86' # IP of Nifi cluster
PORT_NIFI = '8080'       # Port of Nifi cluster
if len(sys.argv) < 2:
    print("Please transmit enough arguments")
    print("EXAMPLE: python3 %s {processorID}" %sys.argv[0])
    exit(1)

ID_PROC   = sys.argv[1]  # ID of Processor in NIFI
cmd = "curl '%s:%s/nifi-api/flow/processors/%s/status/history'" \
      %(IP_NIFI, PORT_NIFI, ID_PROC) 

# Get content of history status log file and store in JSON variable
contents = subprocess.check_output(cmd, shell=True)
jsonFile = json.loads(contents)['statusHistory']['aggregateSnapshots']


for indexJson in range(1, len(jsonFile)):
    curr_mess_count = jsonFile[indexJson]['statusMetrics']['Messages Sent']
    prev_mess_count = jsonFile[indexJson - 1]['statusMetrics']['Messages Sent']
    mess_recv_pmin  = curr_mess_count - prev_mess_count

    print(mess_recv_pmin)
    
