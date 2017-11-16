import numpy as np

a = np.array([range(4), range(10, 14)])
b = np.array([2, -1, 1, 0])

print 'Array a is \n', a
print 'Array b is \n', b

# multiplying arrays
print 'Multiplying element by element gives\n', a * b

b1 = b * 100
b2 = b * 100.0

print 'Array b1 is \n', b1, 'type', b1.dtype
print 'Array b2 is \n', b2, 'type', b2.dtype

print 'b1 == b2 is\n', b1 == b2

# array comparisons
arr = np.array([range(0, 10)])

print 'Condition that array elements are less than 3'
print arr < 3
print np.less(arr, 3)

print 'Condition that array elements are less than 3 and greater than 8'
condition = np.logical_or(arr < 3, arr > 8)
print condition

arr1 = np.where(condition, arr * 5, arr * -5)
print 'New array is\n', arr1



