import matplotlib.pyplot as plt
import matplotlib.patches as patches
import serial
import time

# === Configuración del área de trabajo ===
A = 100  # Ancho del rectángulo
B = 60   # Alto del rectángulo

# === Configura el puerto serial ===
ser = serial.Serial('COM9', 9600)  # Cambia 'COM3' según tu sistema
time.sleep(2)

# === Gráfico ===
plt.ion()
fig, ax = plt.subplots()

# Dibujar el rectángulo
rect = patches.Rectangle((0, 0), A, B, linewidth=1.5, edgecolor='black', facecolor='none')
ax.add_patch(rect)
ax.set_xlim(0, A)
ax.set_ylim(0, B)

# Crear punto inicial (vacío)
point, = ax.plot([], [], 'ro', markersize=8)

try:
    while True:
        
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            try:
                x_str, y_str = line.split(',')
                x = float(x_str)
                y = float(y_str)

                print((x,y))

                # Mostrar punto
                point.set_data([x], [y])
                fig.canvas.draw()
                plt.pause(0.5)

                # Borrar punto (para efecto parpadeante)
                point.set_data([None], [None])
                fig.canvas.draw()
                plt.pause(0.5)

            except ValueError:
                print(f"Dato no válido: {line}")
except KeyboardInterrupt:
    print("Finalizado por el usuario")
    ser.close()
