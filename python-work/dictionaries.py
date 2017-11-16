# dictionaries

band = ['mel', 'geri', 'victoria', 'mel', 'emma']
counts = {}

for (i, member) in enumerate(band):
    counts[i] = member

print counts


# some useful things
if {}:
    print 'hi'

d = {'maggie': 'uk', 'ronnie': 'usa'}

print dir(d)
print 'items:', d.items()
print 'keys:', d.keys()
print 'values:', d.values()

d.setdefault('vladimir', 'russia')

print d
    
