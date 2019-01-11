# cat vt.py
#!/usr/bin/python
import json
import urllib
import time
import pymongo
import sys

APIKEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
str_replace1 = 'u\''
replace_str1 = '\''
str_replace2 = '\''
replace_str2 = '\"'

#import to mongodb
uri = "mongodb://username:password@127.0.0.1/?authSource=dbname&authMechanism=SCRAM-SHA-256"
myconnection = pymongo.MongoClient(uri)
mydb = myconnection["blacklist"]
#mycol = mydb["ip"]
mycol = mydb["dstip_reputation"]


#f = open('ip_failed', 'r+')
f = open('allow3', 'r+')
for ipAddress in f.readlines():
#    print ipAddress.strip()
    a_dict = {'ip': ipAddress.strip()}
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    parameters = {'ip': ipAddress.strip(), 'apikey': APIKEY}
    response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(response)
    response_dict.update(a_dict)
    json1 = str(response_dict).replace(str_replace1, replace_str1)
    json2 = json1.replace(str_replace2, replace_str2)
    print json2

#import to mongodb
    try:
        mycol.insert_one(json.loads(json2))
        print '#########'
        print '#########'
        print '#########'
        print ipAddress.strip()
    except IOError:
        print ('cannot open', mycol)
    except ValueError:
        print ('ValueError', ipAddress.strip())
    except RuntimeError:
        print ('RuntimeError', ipAddress.strip())
#    print 'finished mongodb insert'
    time.sleep(15);
f.close()
myconnection.close()
