# pip install psutil
# pip install pytictoc
from pytictoc import TicToc

t = TicToc()
t.tic()
# ... código a medir ...
t.toc() 
import psutil
import time

dt = 0.1
for i in range(0,10):
    print(psutil.cpu_percent(0.1))
    print(psutil.virtual_memory().percent)
    #print(psutil.sensors_battery())
    time.sleep(dt)

    # TERMINAR EN RPI
