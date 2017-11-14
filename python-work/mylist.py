# Lists and for loops

mylist = [23, "hi", 2.4e-10]
count = 0

while count < 3:
    item = mylist[count]
    print item, 'is at index', str(mylist.index(item))
    count += 1
