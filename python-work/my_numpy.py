# numpy
import numpy as np

# convert a list into an array - e.g., 2D array here
# dtype is optional, defaults to whatever you put in array
# can use to save space, e.g., use int8 not int32

x = range(11)
a1 = np.array(x, dtype = np.int8)
print a1, 'is an array of type', a1.dtype

a2 = np.array(x, dtype=np.float16)
print a2, 'is an array of type', a2.dtype

# zeros - create array of given size (row, col)
# dtype also optional, will default to integers?

b = np.zeros((2, 3, 4), dtype = np.int8)
print b

c = np.ones((2, 3, 4), dtype = np.int8)
print c

# arange

d = np.arange(10)

print d

a = [2, 3.2, 5.5, -6.4, -2.2, 2.4]
print a[1], a[1:4]

# create array with dimensions (3, 6)
a = [a, [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]]

a = np.array(a)
print 'Array a is \n', a
print '\nVarious slices'
print a[:, 3]
print a[1:4, 0:4]
print a[1:, 2]

print '\nArray size is', np.size(a)
print 'Array first dimension (rows) is', np.size(a, 0)
print 'Array second dimension (cols) is', np.size(a, 1)
print 'Array shape is', np.shape(a)
print 'Array rank (number of dimensions) is', np.ndim(a)
print 'Array max is', np.max(a)
print 'Array min is', np.min(a)

# Manipulating arrays
# reshaping
b = np.reshape(a, (9, 2))
print 'Array reshaped to (6, 3) is\n', b

# transpose (can use np.transpose(a) or a.transpose())
c = a.transpose()
print 'Transposed array is\n', c
print 'Array shape is', c.shape

# ravel (flatten to one dimension)
d = np.ravel(a)
print 'Flattened array is\n', d
print 'Array shape is', d.shape

# reshape to 3D
e = a.reshape(2, 3, 3)
print 'Array reshaped to (2, 3, 3) is\n', e

# Convert to int
f = e.astype(np.int8)
print 'Array as int is\n', f

