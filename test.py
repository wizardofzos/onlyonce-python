from oopyconnector import OO

seckey = "your_very_secret_key"
print "SecKey",
seckey = raw_input()
o = OO()

o.apikey='apikey'
o.apisec='apisec'
o.baseurl='http://apiteststand.onlyonce.com'

o.register()
cards = o.cards()

for card in cards:
    print ""
    print "------------------------------------------------------------"
    print "-%s" % card['name']
    print "-%s (owner)       " % card['owner']
    c = o.card(card['id'],seckey)
    print "      %s" % c

