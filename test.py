from oopyconnector import OO, OOCardParser

import datetime
import pprint
import getpass
pp = pprint.PrettyPrinter(indent=4)

seckey = "your_very_secret_key"
o = OO()

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
print "Your API-Key   :",
o.apikey=raw_input()
print "Your API-Secret",
o.apisec=raw_input()
o.apisec = 'henrisec'
o.register()
print " - registered at OOAPI and received bearer token"
cards = o.cards()
print " - fetch all cards shared with me"

keepgoing = True


while keepgoing:
    pos = 0
    for card in cards:
        print "%s - %s" % (pos, card['name'])
        pos += 1

    print "What card to print, X for exit",
    p = raw_input()
    if p == 'X':
        keepgoing = False
    else:
        p = int(p)
        print "Need SecKey (not shown)",
        seckey = getpass.getpass()


        c = o.card(cards[p]['id'],seckey)
        print "-------------------- FULL JSON OF CARD DATA ----------------"
        pp.pprint(c)
        parser = OOCardParser()
        print "-------------------- BASIC INFO FROM CARD (IF ANY)----------"
        print parser.basicInfo(c['data']['model'][0])
        print "<Enter> to continue"
        a = raw_input()

