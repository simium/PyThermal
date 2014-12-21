#!/usr/bin/python

import Image
import time
import datetime
import csv
import thermal_config

millis_at_start = int(round(time.time() * 1000))

temp_data = list(csv.reader(open(thermal_config.files['csv'])))

img = Image.new( 'RGB', (thermal_config.fov['horizontal'],thermal_config.fov['vertical']), "black") # create a new black image
pixels = img.load() # create the pixel map

print 'Processing data: WxH = %dx%d pixels...' % (thermal_config.fov['horizontal'],thermal_config.fov['vertical'])

for i in range(thermal_config.fov['vertical']):
    for j in range(thermal_config.fov['horizontal']):
        t = int(temp_data[i][j])
    
        if t > len(thermal_config.temperatures)-1:
            pixels[j,i] = (255, 255, 255) # set the colour accordingly
        else:
            if thermal_config.options['bw'] == True:
                m = thermal_config.temperature_map(t, 0, 65, 255, 0)
                r = m
                g = m
                b = m
            else:
                r = thermal_config.temperatures[int(temp_data[i][j])][0]
                g = thermal_config.temperatures[int(temp_data[i][j])][1]
                b = thermal_config.temperatures[int(temp_data[i][j])][2]
            pixels[j,i] = (r, g, b) # set the colour accordingly

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H%M%S')

img.save(st+'.bmp', 'BMP')

millis_now = int(round(time.time() * 1000))

if thermal_config.options['bw'] == True:
    print 'Thermal B/W image generated: %s, took %d ms' % (st+'.bmp', millis_now - millis_at_start)
else:
    print 'Thermal color image generated: %s, took %d ms' % (st+'.bmp', millis_now - millis_at_start)

