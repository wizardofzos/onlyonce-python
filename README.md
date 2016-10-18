# onlyonce-python

*The Unofficial python framework to connect to the Only Once API*

---

_Author_ : **Henri Kuiper** 

_Planned Official Release Date_   : **2017-01-01** 

_Version_ : 0.78.23, status: **Draft**

## NOT READY FOR PRODUCTION 



## Installation
    /* mkvirtualenv if you have to */
    pip install onlyonce-python
    
## Basic Usage Scheme

    from oopyconnector import OO

    
    o = OO()

  
    o.baseurl='https://api.onlyonce.com'
    o.username = os.environ.get('oouser')
    o.password = os.environ.get('oopass')


    o.signin()
    profiles = o.profiles()
    for profile in profiles:
      all_cards = o.cards(profile=profile['id'])
      
### Try it via
    make test
## Functions
---

# Get Token
Function : *signin()* - **Get your JWT Bearer Token**

    oo.singin()


Make sure to set o.apikey and o.apisec before calling register(). The register function will set the Authorization Header in your request with the Bearer Token.

# Get Cards
Function : *cards()* - **Get all cards shared with you**

    oo.cards()


Only callable after a succesful register(). It will return index of all cards shared with you. Returns a list of card-objects.

    {'name' : "<card_name>",
     'owner': "<card_owner>"
     'id'   : "<the-card-id-for-your-api-call>"
    }
    
These can be read with card(id, seckey) sending your "Secret-Key" in the header of the request.

# Get Card
Function : *card(id)* - **Get the content of a card**

    card(id)


Only callable after succesful register() it requries the access_required endpoint too :)
It will return the card and it's model.

    


