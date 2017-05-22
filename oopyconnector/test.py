from oopyconnector import OO
import os
import pprint
import json
import datetime

pp = pprint.PrettyPrinter(indent=2)


print "              _                            "
print "   ___  _ __ | |_   _  ___  _ __   ___ ___ "
print "  / _ \| '_ \| | | | |/ _ \| '_ \ / __/ _ \\"
print " | (_) | | | | | |_| | (_) | | | | (_|  __/"
print "  \___/|_| |_|_|\__, |\___/|_| |_|\___\___|"
print "                |___/                      "
print ""
print " testing oopyconnector                     "
print ""
print " make sure to set oouser, oopass and oosec "
print " we know it's annoying to set the secret   "
print " before you an select the profile, but hey,"
print " security > usability :)                   "
print ""

def show(consolidated, *args, **kwargs):
    # print consolidated
    for c in consolidated['content']:
        for key in c.keys():
            fname = unicode(c[key]['first_name_field']).encode('utf8')
            if c[key]['middle_name_field']:
                mname = unicode(c[key]['middle_name_field']).encode('utf8')
            else:
                mname = None
            lname = unicode(c[key]['last_name_field']).encode('utf8')
            email = unicode(c[key]['communication_email1_field']).encode('utf8')
            print "fname: " + fname
            if mname:
                print "mname: " + mname
            print "lname: " + lname
            print "email: " + email
o = OO()

o.baseurl = 'https://api.onlyonce.com'

if os.environ.get('oouser') and os.environ.get('oopass') and os.environ.get('oosec'):
    print "Using credentials as specified in ENV"
    o.username = os.environ.get('oouser')
    o.password = os.environ.get('oopass')
    o.seckey = os.environ.get('oosec')
else:
    raise Exception, "Cannot Continue. You need to specify oouser, oopass and oosec as environment variables. We did tell you so :)"

o.signin()

print "Signin OK!"
print ""
print ""
#o.signout()

profiles = o.profiles()

print "Welcome %s, you are fully authorized for these profiles" % o.username
print "----------------"
print ""
i = 0
pids = []
for p in profiles:
    pids.append(p['id'])
    print "%s) %s [%s %s %s in, %s out]" % (i, p['name'],p['type'], p['kind'],p['inc'],p['out'])
    i += 1

print ""
print "----------------"
print ""

print "Select profile to work with: ",
prof = raw_input()


fields = [ "first_name_field", "middle_name_field", "last_name_field",
           "communication_email1_field",
           "date_of_birth_field",
           "trade_name_field"]


consolidated = o.consolidated(profileId=pids[int(prof)], fieldNames=fields)
fetched = len(consolidated['content'])
print "Retrieved first page, executing GoogleSync %s fetched" % fetched
show(consolidated)

page = 0
res = consolidated['content']
while not consolidated['last']:

    page += 1
    print "Next page..."
    consolidated = o.consolidated(profileId=pids[int(prof)], fieldNames=fields, page=page)
    fetched += len(consolidated['content'])
    show(consolidated)
    res.append(consolidated['content'])

print "All %s results parsed!!!" % fetched














