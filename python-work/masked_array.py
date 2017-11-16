import numpy as np
import numpy.ma as MA

marr = MA.masked_array(range(0, 10), fill_value = -999)
print marr

marr[2] = MA.masked
print marr, marr.mask

narr = MA.masked_where(marr > 6, marr)
print narr, narr.mask, narr.fill_value

x = MA.filled(narr)
print x, type(x)

# mask smaller than array
m1 = MA.masked_array(range(1, 9))
print m1

m2 = m1.reshape((2, 4))
print m2

m3 = MA.masked_where(m2 > 6, m2)
print m3

print m3 * 100

m4 = np.ones((2, 4), np.int8)
print m4

res = m3 -m4
print res
print type(res)
