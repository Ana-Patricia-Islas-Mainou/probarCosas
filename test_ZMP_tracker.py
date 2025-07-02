import matplotlib.pyplot as plt
import matplotlib.patches as patches
import serial
import time

# === Foot Size ===
A = 100  # width
B = 200   # lenght

# == Sensor Locations ==


try:
    ser = serial.Serial('COM9', 9600)  # Cambia 'COM3' según tu sistema
    print("Port configured and opened correclty")
except:
    print("Error opening serial port")
    print("Check COM number and conection")
    quit()
time.sleep(2)

# === Plots ===
plt.ion()
fig, ax = plt.subplots()

# Feet description
rfoot = patches.Rectangle((10, -B/2), A, B, linewidth=1.5, edgecolor='black', facecolor='none')
lfoot = patches.Rectangle((-10, B/2), -A, -B, linewidth=1.5, edgecolor='black', facecolor='none')

ax.add_patch(rfoot)
ax.add_patch(lfoot)
lim_size = 150
ax.set_xlim(-lim_size, lim_size)
ax.set_ylim(-lim_size, lim_size)

# define ZMP location based on serial data
point, = ax.plot([], [], 'ro', markersize=8)

try:
    while True:
        if ser.in_waiting > 0:
            # read serial data
            line = ser.readline().decode('utf-8').strip()
            try:
                # separate data
                x_str, y_str = line.split(',')
                x = float(x_str)
                y = float(y_str)
                print((x,y))

                # update point
                point.set_data([x], [y])
                fig.canvas.draw()
                
                plt.pause(0.05)

            except ValueError:
                print(f"Non Valid Data: {line}")

except KeyboardInterrupt:
    print("Program Terminated by User")
    ser.close()
