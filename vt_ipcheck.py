#!/usr/bin/python
import json
import urllib
import time

APIKEY=''
str_replace1 = 'u\''
replace_str1 = '\''
str_replace2 = '\''
replace_str2 = '\"'


f = open('ip_failed', 'r+')
for ipAddress in f.readlines():
    print ipAddress.strip()
    a_dict = {'ip': ipAddress.strip()}
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    parameters = {'ip': ipAddress.strip(), 'apikey': APIKEY}
    response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(response)
    response_dict.update(a_dict)
    json1 = str(response_dict).replace(str_replace1, replace_str1)
    print json1.replace(str_replace2, replace_str2)
    time.sleep(15);
f.close()
