#!/usr/bin/python
import json
import urllib
import time

APIKEY=''

f = open('ip_failed', 'r+')
for ipAddress in f.readlines():
    print ipAddress.strip()
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    parameters = {'ip': ipAddress.strip(), 'apikey': 'APIKEY'}
    response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(response)
    print response_dict
    time.sleep(15);
f.close()
