# tuples

# Create tuple containing all values from 100 to 200
# Create list with range from 100 to 200
x = range(100, 201)

# convert to tuple
y = tuple(x)

print y

# print first and last items in tuple
print y[0], y[-1]

# enumerate function
mylist = [23, "hi", 2.4e-10]

for (count, item) in enumerate(mylist):
    print count, item

# list to tuple
(first, middle, last) = mylist
print first, middle, last

(first, middle, last) = 'last', 'middle', 'first'
print first, middle, last


