from oopyconnector import OO
import os



o = OO()
o.baseurl = 'https://api.onlyonce.com'
if os.environ.get('oouser') and os.environ.get('oopass') and os.environ.get('oosec'):
    print "all here"
    o.username = os.environ.get('oouser')
    o.password = os.environ.get('oopass')
else:
    print "nope"

    print "Your username (email) please [shown]"
    o.username = raw_input()
    print "Your password please [shown]"
    o.password = raw_input()

o.signin()

print "Signin OK!"
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
    print "%s) %s [%s %s]" % (i, p['name'],p['type'], p['kind'])
    i += 1

print ""
print "----------------"
print ""

print "Select profile to work with: ",
prof = raw_input()

print ""
print "----------------"
print ""

all_cards = o.cards(profile=pids[int(prof)])
i = 0
cards = []

from operator import itemgetter
all_cards = sorted(all_cards, key=itemgetter('owner'))
for c in all_cards:
    cards.append(c['id'])
    print "%s) %s [%s]" % (i, c['owner'],c['name'])
    i += 1

print ""
print "----"
print ""

print "You have a total of %s cards" % len(cards)

print "Compressing your cards to create consolidated view of your network"









