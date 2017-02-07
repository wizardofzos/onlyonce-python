from oopyconnector import OO, OOCardParser
import os
import pprint
import datetime
import sys

pp = pprint.PrettyPrinter(indent=2)


print "              _                            "
print "   ___  _ __ | |_   _  ___  _ __   ___ ___ "
print "  / _ \| '_ \| | | | |/ _ \| '_ \ / __/ _ \\"
print " | (_) | | | | | |_| | (_) | | | | (_|  __/"
print "  \___/|_| |_|_|\__, |\___/|_| |_|\___\___|"
print "                |___/                      "
print ""
print " Command line demonstration of the OO-API  "
print ""




o = OO()
ocp = OOCardParser()

o.baseurl = 'http://apiteststand.onlyonce.com'

if os.environ.get('oouser') and os.environ.get('oopass') and os.environ.get('oosec'):
    print "Using credentials as specified in ENV"
    o.username = os.environ.get('oouser')
    o.password = os.environ.get('oopass')
    o.seckey = os.environ.get('oosec')
else:
    raise Exception, "Cannot Continue. You need to specify oouser, oopass and oosec as environment variables"

o.signin()

print ""
print ""

profiles = o.profiles()

print "Welcome %s, you are fully authorized for these profiles" % o.username
print "----------------"
print ""
i = 0
pids = []
for p in profiles:
    pids.append(p['id'])
    print "%s) %s, #%s [%s %s %s in, %s out]" % (i, p['name'],p['ooid'],p['type'], p['kind'],p['inc'],p['out'])
    i += 1

print ""
print "----------------"
print ""

print "Select profile to work with: ",
prof = raw_input()

r = o.getRequests(pids[int(prof)], reqtype="INCOMING", status="PENDING")
if r['content']:
    for req in r['content']:
        pp.pprint(req)
        o.acceptRequest(req['id'])
else:
    print "no requests"

