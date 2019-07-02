import datetime
from tailer import tail
from os import mkdir,path

# Attribute to read log file
HOME_NIFI = '/home/kienpham/nifi/logs-benchmark'
if not path.exists(HOME_NIFI):
    mkdir(HOME_NIFI)
ADDRESS = '/home/kienpham/nifi/logs/log-mess.log'
timelst = list()
lines = list()
# Start to read file

logfile = open(ADDRESS, 'r')
timestp = str(datetime.datetime.today())

last_line = str(tail(logfile, 1)[0])
CONTENT = last_line[-8:] 

for line in tail(logfile, 100000):
    # Read timestamp
    timestamp = datetime.datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S,%f')
    # Read code of test
    content = line[-8:]
    if content == CONTENT:
        lines.append(line)
        timelst.append(timestamp)
        CONTENT = content

if len(timelst) >= 64000:
    print(CONTENT)
    print('1000  :' + str(datetime.timedelta.total_seconds(timelst[-1] - timelst[-1000])))
    print('2000  :' + str(datetime.timedelta.total_seconds(timelst[-1] - timelst[-2000])))
    print('4000  :' + str(datetime.timedelta.total_seconds(timelst[-1] - timelst[-4000])))
    print('8000  :' + str(datetime.timedelta.total_seconds(timelst[-1] - timelst[-8000])))
    print('16000 :' + str(datetime.timedelta.total_seconds(timelst[-1] - timelst[-16000])))
    print('32000 :' + str(datetime.timedelta.total_seconds(timelst[-1] - timelst[-32000])))
    print('64000 :' + str(datetime.timedelta.total_seconds(timelst[-1] - timelst[-64000])))


if str(content).__contains__("HTTP"):
    if not path.exists(HOME_NIFI + '/http'):
        mkdir(HOME_NIFI + '/http')
    with open(HOME_NIFI + '/http/'+ content.lower().replace('[', '').replace(']', '-') + '-' + timestp, 'w') as outFile:
        outFile.writelines('\n'.join(lines))
elif str(content).__contains__("TCP"):
    if not path.exists(HOME_NIFI + '/tcp'):
        mkdir(HOME_NIFI + '/tcp')
    with open(HOME_NIFI + '/tcp/'+ content.lower().replace('[' , '').replace(']', '-') + '-' + timestp, 'w') as outFile:
        outFile.writelines('\n'.join(lines))
elif str(content).__contains__("UDP"):
    if not path.exists(HOME_NIFI + '/udp'):
        mkdir(HOME_NIFI + '/udp')
    with open(HOME_NIFI + '/udp/'+ content.lower().replace('[' , '').replace(']', '-') + '-' + timestp, 'w') as outFile:
        outFile.writelines('\n'.join(lines))
elif str(content).__contains__("MQTT"):
    if not path.exists(HOME_NIFI + '/mqtt'):
        mkdir(HOME_NIFI + '/mqtt')
    with open(HOME_NIFI + '/mqtt/' + content.lower().replace('[' , '').replace(']', '-') + '-' + timestp, 'w') as outFile:
        outFile.writelines('\n'.join(lines))

logfile.close()