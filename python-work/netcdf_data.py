from netCDF4 import Dataset

dataset = Dataset('example_data/ggas2014121200_00-18.nc')
keys = dataset.variables.keys()

print 'Convention:', dataset.Conventions

print 'Keys:'
for key in keys:
    print '\t', key

sst = dataset.variables['SSTK']

print 'SST variables:\n', sst

print 'SST variable dimensions:'
for dim in sst.dimensions:
    print '\t', dim, len(dataset.variables[dim])

print 'SST shape:', sst.shape
print 'SST size:', sst.size

print 'SST attributes:'
metadata = {}
for attr in sst.ncattrs():
    print '\t', attr
    metadata[attr] = getattr(sst, attr)

# Get slice of SST data
arr = sst[1, 0, 10:20, 30:35]

print 'arr has type of ', type(arr)
dims = sst.dimensions
print dims
vars = dataset.variables

arr_time = vars['time'][1]
arr_level= vars['surface'][0]
arr_lats = vars['latitude'][10:20]
arr_longs = vars['longitude'][30:35]

for vals in (arr_time, arr_level, arr_lats, arr_longs):
    print vals

