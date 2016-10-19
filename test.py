
import datetime
import pprint
import getpass
pp = pprint.PrettyPrinter(indent=4)

seckey = "your_very_secret_key"
o = OO()


print "              _                            "
print "   ___  _ __ | |_   _  ___  _ __   ___ ___ "
print "  / _ \| '_ \| | | | |/ _ \| '_ \ / __/ _ \\"
print " | (_) | | | | | |_| | (_) | | | | (_|  __/"
print "  \___/|_| |_|_|\__, |\___/|_| |_|\___\___|"
print "                |___/                      "
print ""
print " Command line demonstration of the OO-API  "
print ""

import oopyconnector

o = OO()


o.baseurl='https://api.onlyonce.com'
o.username = os.environ.get('oouser')
o.password = os.environ.get('oopass')


o.signin()
profiles = o.profiles()
for profile in profiles:
      all_cards = o.cards(profile=profile['id'])
