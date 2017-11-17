from example_code.map_data import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig = plt.figure()

m = Basemap(projection = 'cyl', llcrnrlat = -90, urcrnrlat = 90, llcrnrlon = -180, urcrnrlon = 180, resolution = 'c')
m.drawcoastlines()
im1 = m.pcolormesh(lons, lats, tas, shading = 'flat', cmap = plt.cm.jet, latlon = True)
plt.pause(15)

plt.savefig('tas1.png')
