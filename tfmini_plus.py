from __future__ import division, print_function
from tfmini import TFmini  # Used TFmini Plus LiDAR
import time

# create the sensor and give it a port and (optional) operating mode
tf = TFmini('/dev/ttyUSB0', mode=TFmini.STD_MODE)

try:
    print('='*25)
    while True:
        d = tf.read()
        if d:
            print('Distance: {:5}m '.format(d))
        else:
            print('No valid response')
        time.sleep(0.1)

except KeyboardInterrupt:
    tf.close()
    print('bye!!')

