# file input/output
import struct

# read entire file
with open('weather.csv', 'r') as reader:
    data = reader.read()

print len(data)
print data

# read line by line
with open('weather.csv', 'r') as reader:
    line = reader.readline()
    print line

    while line != '':
        line = reader.readline()
        print line

print "It's over"

# get rainfall value using a for loop
print '\nGet rainfall values'
with open('weather.csv', 'r') as reader:
    header = reader.readline()
    rain = []

    for line in reader:
        split_line = line.strip().split(',')
        rainfall = float(split_line[-1])
        rain.append(rainfall)

print rain

with open('myrain.txt', 'w') as writer:
    writer.write('Rainfall\n')
    
    for r in rain:
        writer.write(str(r) + '\n')

# read/write binary data
bin_data = struct.pack("bbbb", 123, 12, 45, 34)

with open('mybinary.dat', 'wb') as writer:
    writer.write(bin_data)

with open('mybinary.dat', 'rb') as reader:
    bin_data2 = reader.read()

data = struct.unpack("bbbb", bin_data2)
print data

