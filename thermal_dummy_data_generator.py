#!/usr/bin/python

import random
import thermal_config
import csv
import time

millis_at_start = int(round(time.time() * 1000))

random_temp_2d_list = []

tmin = thermal_config.temperature['tmax']
tmax = thermal_config.temperature['tmin']

for i in range(thermal_config.fov['vertical']): # for every scanned pixel/degree:
    pixels = []
    for j in range(thermal_config.fov['horizontal']):
        t = random.randint(thermal_config.temperature['tmin'], thermal_config.temperature['tmax'])
        
        if t > tmax:
            tmax = t
        if t < tmin:
            tmin = t
        
        pixels.append(t)
    random_temp_2d_list.append(pixels)

with open(thermal_config.files['csv'], 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(random_temp_2d_list)

millis_now = int(round(time.time() * 1000))

print 'Generated a %dx%d measures array ' \
      'between %d and %d (min=%d, max=%d), ' \
      'took %d ms' \
      % (thermal_config.fov['horizontal'], thermal_config.fov['vertical'],
         thermal_config.temperature['tmin'], thermal_config.temperature['tmax'],
         tmin, tmax,
         millis_now - millis_at_start)
    
