# strings...

# looping through string as a sequence
s = 'I love to write python'

for char in s:
    print char

print 'Fifth character:', s[4]
print 'Last character:', s[-1]
print 'Length of string', len(s)

print s[0], s[0][0], s[0][0][0]

# splitting a string into words
split_s = s.split(' ')

for word in split_s:
    if word.lower().find('i') > -1:
        print "I found 'i' in: " + word

# more stringy stuff
something = 'Completely Different'
# print dir(something)
print 'Contains', something.count('t'), "t's"
print something.find('plete')

something_split = something.split('e')
print something_split

thing2 = something.replace('Different', 'Silly')
print thing2

# this does not work as strings are immutable...
# something[0] = 'B'
