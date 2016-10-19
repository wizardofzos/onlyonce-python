from oopyconnector import OO, OOCardParser
import os
import pprint

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

o.baseurl = 'https://api.onlyonce.com'
if os.environ.get('oouser') and os.environ.get('oopass') and os.environ.get('oosec'):
    print "Using credentials as specified in ENV"
    o.username = os.environ.get('oouser')
    o.password = os.environ.get('oopass')
    o.seckey = os.environ.get('oosec')
else:
    raise Exception, "Cannot Continue. You need to specify oouser, oopass and oosec as environment variables"

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

print ""
print "----------------"
print ""

#datastore = o.datastore(profile=pids[int(prof)])
#pp.pprint(datastore)



all_cards = o.cards(profile=pids[int(prof)])
i = 0
cards = []

# Nice "blackmagic" to sort the list of json-objects on a specified key
from operator import itemgetter
all_cards = sorted(all_cards, key=itemgetter('owner'))


for c in all_cards:
    cards.append(c['id'])
    owningProfile = o.profile(c['owner'])
    print "%s) %s/#%s [%s]" % (i, owningProfile['name'], owningProfile['onlyonceId'],c['name'])
    card = o.card(profileid = pids[int(prof)], cardid = c['id'])
    #try:
    #    pp.pprint(card)
    #except:
    #    print "eeek"
    print('------')
    #pp.pprint(ocp.basicInfo(card))
    ##pp.pprint(ocp.getInfo(card,['job_position_field']))
    i += 1

print ""
print "----"
print ""

print "You have a total of %s cards" % len(cards)

print "What card to print?"
cd = raw_input()

print o.card(pids[int(prof)], cards[int(cd)])
print "Compressing your cards to create consolidated view of your network"

print "Make sure we access enable the profile"











