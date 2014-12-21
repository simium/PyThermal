#!/usr/bin/python

import random
import thermal_config as tcfg
import csv
import time

millis_at_start = int(round(time.time() * 1000))

random_temp_2d_list = []

tmin = tcfg.temperature['tmax']
tmax = tcfg.temperature['tmin']

for i in range(tcfg.fov['vertical']):
    pixels = []
    for j in range(tcfg.fov['horizontal']):
        t = random.randint(tcfg.temperature['tmin'], tcfg.temperature['tmax'])
        if t > tmax:
            tmax = t
        if t < tmin:
            tmin = t
        pixels.append(t)
    random_temp_2d_list.append(pixels)

with open(tcfg.files['csv'], 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(random_temp_2d_list)

millis_now = int(round(time.time() * 1000))

print 'Generated a %dx%d measures array ' \
      'between %d and %d (min=%d, max=%d), ' \
      'took %d ms' \
      % (tcfg.fov['horizontal'], tcfg.fov['vertical'],
         tcfg.temperature['tmin'], tcfg.temperature['tmax'],
         tmin, tmax,
         millis_now - millis_at_start)
