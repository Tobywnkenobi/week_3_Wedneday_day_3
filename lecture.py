# Dylan's white board solution:

def replace_fire(astring):
    return ' '.join(map(lambda word: word if word != 'Fire' else '~~',astring.split()))

print(replace_fire( "Biat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast"))

