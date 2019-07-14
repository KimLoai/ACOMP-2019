#!/usr/bin/python

import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
import time
from zabbix.api import ZabbixAPI

# argument check
if len(sys.argv) < 2:
  print "USAGE: zabbixURL user pass host itemName"
  print "EXAMPLE: http://127.0.0.1/zabbix Admin zabbix myhost mystr1"
  sys.exit(1)

# simple parse for arguments
# url = "http://hpcc.hcmut.edu.vn:61112"
url = "http://10.28.8.119/zabbix"
user = "admin"
password = "zabbix"
host = sys.argv[1]
key = sys.argv[2]
print "Going to connect to {} as {}, and retrieve from host {} the item {}".format(url,user,host,key)


# Create ZabbixAPI class instance
use_older_authenticate_method = False
zapi = ZabbixAPI(url, use_older_authenticate_method, user, password)

zversion = zapi.do_request('apiinfo.version')
print "Zabbix API version: {}".format(zversion['result'])


# https://www.zabbix.com/documentation/2.2/manual/api/reference/host/get
# Get specified host
print "----------------------------"
thehost = zapi.do_request('host.get',
                          {
                              'filter': {'host': host},
                              'selectItems' : 'extend',
                              'output': 'extend'
                          })
if len(thehost['result'])<1:
  print "HALTING. There was no host defined in zabbix with id: {}".format(host)
  sys.exit(2)
hostId = thehost['result'][0]['hostid']
print "Found host {} with id {}".format(host,hostId)

# now look for item within that host
itemId = None
for item in thehost['result'][0]['items']:
  # for debugging
  #print "item[{}] -> {}".format(item['itemid'],item['key_'])
  # if match, then get out int id and type (0=float,1=char,3=unsign,4=text)
  if item['key_'] == key:
    itemId = item['itemid']
    itemType = item['value_type']
if itemId is None:
  print "HALTING. There was no item defined on host {} with name: {}".format(host,key)
  sys.exit(2)
print "Found item {} on host {} with item id/type {}/{}".format(key,host,itemId,itemType)


# https://www.zabbix.com/documentation/2.2/manual/api/reference/history/get
print "----------------------------"
history = zapi.do_request('history.get',
                          {
                              'history': itemType,
                              'filter': {'host': host, 'itemid': itemId},
                              'limit': '1000',
                              'sortfield': 'clock',
                              'sortorder': 'DESC',
                              'output': 'extend'
                          })
# show history rows 
print "Retrieved {} rows of history".format(len(history['result']))
with open(key + ".csv", 'w') as outFile:
  outFile.write("index" + ',' + "time" + ',' + "value" + '\n')
  for hist in history['result'][::-1]:
    # convert epoch to human readable format
    timestr = time.strftime('%H:%M:%S', time.localtime(long(hist['clock'])))
    outFile.write("{}, {}, {}\n".format(len(history['result']) - history['result'].index(hist), timestr, hist['value']))
