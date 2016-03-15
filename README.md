# onlyonce-python

*The Unofficial python framework to connect to the Only Once API*

---

_Author_ : **Henri Kuiper** 

_Planned Official Release Date_   : **2016-04-01** 

_Version_ : **Draft**



## Installation
    /* mkvirtualenv if you have to */
    pip install onlyonce-python
    
## Basic Usage Scheme

    from oopyconnector import OO

    seckey = "your_very_secret_key"
    o = OO()

    o.apikey='apikey'
    o.apisec='apisec'
    o.baseurl='https://api.onlyonce.com'

    o.register()
    cards = o.cards()

    for card in cards:
        print "------%s" % card['name']
        print "      %s (owner)       " % card['owner']
        c = o.card(card['id'],seckey)
        print "      %s" % c

### Try it via
    make test
## Functions
---

# Get Token
Function : *register()* - **Get your JWT Bearer Token**

Make sure to set o.apikey and o.apisec before calling register(). The register function will set the Authorization Header in your request with the Bearer Token.

# Get Cards
Function : *cards()* - **Get all cards shared with you**

Only callable after a succesful register(). It will return index of all cards shared with you. Returns a list of card-objects.

    {'name' : "<card_name>",
     'owner': "<card_owner>"
     'id'   : "<the-card-id-for-your-api-call>"
    }
    
These can be read with card(id, seckey) sending your "Secret-Key" in the header of the request.

# Get Card
Function : *card(id, seckey)* - **Get the content of a card**

Only callable after succesful register(). It will return the card.

    


