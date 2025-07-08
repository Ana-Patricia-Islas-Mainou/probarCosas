# pip install psutil

import psutil
import time

dt = 0.1
for i in range(0,10):
    print(psutil.cpu_percent(0.1))
    print(psutil.virtual_memory().percent)
    #print(psutil.sensors_battery())
    time.sleep(dt)

    # TERMINAR EN RPI
