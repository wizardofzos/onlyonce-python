from oopyconnector import OO

import datetime
import pprint
pp = pprint.PrettyPrinter(indent=4)

seckey = "your_very_secret_key"
o = OO()

o.apikey='apikey'
o.apisec='apisec'
o.baseurl='http://apiteststand.onlyonce.com'

print "              _                            "
print "   ___  _ __ | |_   _  ___  _ __   ___ ___ "
print "  / _ \| '_ \| | | | |/ _ \| '_ \ / __/ _ \\"
print " | (_) | | | | | |_| | (_) | | | | (_|  __/"
print "  \___/|_| |_|_|\__, |\___/|_| |_|\___\___|"
print "                |___/                      "
print ""
print " Command line demonstration of the OO-API  "
print ""
o.register()
print " - registered at OOAPI and received bearer token"
cards = o.cards()
print " - fetch all cards shared with me"


pos = 0
for card in cards:
    print "%s - %s" % (pos, card['name'])
    pos += 1

print "What card to print",
p = int(raw_input())

print "Need SecKey (shown)",
seckey = raw_input()

c = o.card(cards[p]['id'],seckey)
pp.pprint(c)





