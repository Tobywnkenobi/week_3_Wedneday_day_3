'''
# On vacation in the Bahamas you decide to go out on a scuba trip one day.

# Unfortunately, disaster has struck!! The boat has caught fire!!

# You will be provided a string that lists many boat related items. Make a function called replace_fire that takes in a string (input) and if any of these items are "Fire" you must spring into action. Change any instance of "Fire" into "~~". Then return the string .

# input: "Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast",

# output: "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast

'''

import re
def fire_fighter(astring):
    return re.sub(r'\bFire\b','~~',astring)