#!/usr/bin/python

import thermal_config as tcfg
import numpy as np
import csv
import time

millis_at_start = int(round(time.time() * 1000))

random_temp_2d_matrix = np.random.randint(tcfg.temperature['tmax'],
                                          size=(tcfg.fov['vertical'],
                                                tcfg.fov['horizontal']))

with open(tcfg.files['csv'], 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(random_temp_2d_matrix)

millis_now = int(round(time.time() * 1000))

print 'Generated a %dx%d measures array ' \
      'between %d and %d, ' \
      'took %d ms' \
      % (tcfg.fov['horizontal'], tcfg.fov['vertical'],
         tcfg.temperature['tmin'], tcfg.temperature['tmax'],
         millis_now - millis_at_start)
