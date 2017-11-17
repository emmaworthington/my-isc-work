import numpy as np
import datetime
from netCDF4 import Dataset 
from csv import reader

def get_time(time):
    value = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
    return value

def get_temp_kelvin(temp_c):
    value = temp_c.strip('+').strip('C').lstrip('0')
    return float(value) + 273.15

infile = 'temps_save.tsv'
outfile = 'my_sensor_data.nc'

times = []
temps = []

with open(infile, 'rb') as tsvfile:
    tsvreader = reader(tsvfile, delimiter = '\t')

    for row in tsvreader:
        times.append(get_time(row[0]))
        temps.append(get_temp_kelvin(row[1]))

for (i, time) in enumerate(times):
    print time, temps[i], '\n'


