import copy
# aliasing

# lists
a = [0, 1, 2]
b = a

print a
print b

b[0] = 'hello'

print a
print b

a.append(3)

print a
print b

# strings
a = 'can I change'
b = a

print a
print b

b = 'different'

print a
print b

# deep copy - makes a full copy without aliasing
a = [0, 1, 2]
b = copy.deepcopy(a)

print a
print b

b[0] = 'hello'

print a
print b
