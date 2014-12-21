#!/usr/bin/python

import Image
import time
import datetime
import csv
import thermal_config as tcfg

millis_at_start = int(round(time.time() * 1000))

temp_data = list(csv.reader(open(tcfg.files['csv'])))

img = Image.new('RGB', (tcfg.fov['horizontal'], tcfg.fov['vertical']), "black")
pixels = img.load()

print 'Processing data: WxH = %dx%d pixels...' \
      % (tcfg.fov['horizontal'], tcfg.fov['vertical'])

for i in range(tcfg.fov['vertical']):
    for j in range(tcfg.fov['horizontal']):
        t = int(temp_data[i][j])
        if t > len(tcfg.temperatures)-1:
            pixels[j, i] = (255, 255, 255)
        else:
            if tcfg.options['bw'] is True:
                m = tcfg.temperature_map(t, 0, 65, 255, 0)
                r = m
                g = m
                b = m
            else:
                r = tcfg.temperatures[int(temp_data[i][j])][0]
                g = tcfg.temperatures[int(temp_data[i][j])][1]
                b = tcfg.temperatures[int(temp_data[i][j])][2]
            pixels[j, i] = (r, g, b)
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H%M%S')

img.save(st+'.bmp', 'BMP')

millis_now = int(round(time.time() * 1000))

if tcfg.options['bw'] is True:
    print 'Thermal B/W image generated: %s, took %d ms' \
          % (st+'.bmp', millis_now - millis_at_start)
else:
    print 'Thermal color image generated: %s, took %d ms' \
          % (st+'.bmp', millis_now - millis_at_start)
