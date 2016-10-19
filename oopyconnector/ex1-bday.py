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

o.baseurl = 'https://api.onlyonce.com'
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

print ""
print "  Getting your networks birthdays......"
print ""
print """
  #####                                        ######
 #     # ###### ##### ##### # #    #  ####     #     # # #####  ##### #    # #####    ##   #   #  ####
 #       #        #     #   # ##   # #    #    #     # # #    #   #   #    # #    #  #  #   # #  #
 #  #### #####    #     #   # # #  # #         ######  # #    #   #   ###### #    # #    #   #    ####
 #     # #        #     #   # #  # # #  ###    #     # # #####    #   #    # #    # ######   #        #
 #     # #        #     #   # #   ## #    #    #     # # #   #    #   #    # #    # #    #   #   #    #
  #####  ######   #     #   # #    #  ####     ######  # #    #   #   #    # #####  #    #   #    ####
"""





all_cards = o.cards(profile=pids[int(prof)])
i = 0
cards = []

birthdays = {}
network = {}

# Nice "blackmagic" to sort the list of json-objects on a specified key
from operator import itemgetter
all_cards = sorted(all_cards, key=itemgetter('owner'))
card_data = []
print str(datetime.datetime.now()) + " - Getting (and decrypting) all your cards plus owning profile if not there already.  "
for c in all_cards:
    cards.append(c['id'])
    print str(len(cards)) + " ",
    if network.has_key(c['owner']):
        owningProfile = network[c['owner']]
    else:
        owningProfile = o.profile(c['owner'])
        network[c['owner']] = owningProfile
    # Skip broken cards here (buggy but ok)
    if owningProfile['name'] == "Hans van der Let":
        print "broken card by Hans van der Let due to API/APP mismatch. Skip!"
    else:
        if not birthdays.has_key(c['owner']):
            print repr(c['name']) + " - " + repr(owningProfile['name'])
            card = o.card(profileid = pids[int(prof)], cardid = c['id'])
            if len(card['model']) == 1:
                card_data.append(card)
                bday = ocp.getInfo(card,['first_name_field', 'date_of_birth_field'])
                if bday['date_of_birth_field']:
                    birthdays[c['owner']] = bday['date_of_birth_field']
        else:
                print "optimistic skip, have birthday already"

print str(datetime.datetime.now()) + " - Done getting and decrypting your networks data"
print ""
print "----"
print ""


print "Birthdays ready!"

for who in birthdays:
    bd = birthdays[who].split('-')
    dob = datetime.datetime.strptime(birthdays[who], "%d-%m-%Y")
    dt = datetime.datetime.now()
    dd = dt - dob
    tyb = datetime.datetime.strptime("%s-%s-%s" % (dob.day, dob.month, dt.year), "%d-%m-%Y")
    dtb = tyb - dt
    print "%s\t\t\t\t\t\tborn on %s is \t%s days old. \t(%s days from birthday)" % (repr(network[who]['name']), birthdays[who], dd.days, dtb.days + 1)

    # normies varnames
    contact = network[who]
    birthday = birthdays[who]


    if dtb.days > 0 and dtb.days <= 14:
        print repr(contact['name']) + "BIRTHDAY WITHIN 2 WEEKS"













