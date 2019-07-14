import os
import sys
import datetime
import subprocess

topic = sys.argv[1]
cmd = "$KAFKA_HOME/bin/kafka-run-class.sh kafka.tools.GetOffsetShell \
       --broker-list localhost:9092 --topic %s" %(topic)

while True :
    print(datetime.datetime.now())
    os.system(cmd)
