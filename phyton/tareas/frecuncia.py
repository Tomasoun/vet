import numpy as np
import sounddevice as sd

# Parámetros
frecuencia = 440  # Frecuencia en Hz (La4)
duracion = 3.0    # Duración en segundos
amplitud = 0.5    # Amplitud (0 a 1)
tasa_muestreo = 44100  # Tasa de muestreo en Hz

# Generar onda sinusoidal
t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False)
tono = amplitud * np.sin(2 * np.pi * frecuencia * t)

# Reproducir el sonido
sd.play(tono, tasa_muestreo)
sd.wait()  # Esperar hasta que termine la reproducción

import numpy as np
import sounddevice as sd

# Parámetros generales
nota_base = 440  # La4
duracion = 0.5   # medio segundo por nota
amplitud = 0.5
tasa_muestreo = 44100

# Intervalos de la escala mayor (en semitonos)
intervalos = [0, 1, 4, 5, 7, 8, 11, 12]  # Desde La4 hasta La5

# Reproducción de cada nota
for i in intervalos:
    freq = nota_base * (2 ** (i / 12))  # calcular frecuencia
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False)
    tono = amplitud * np.sin(2 * np.pi * freq * t)
    sd.play(tono, tasa_muestreo)
    sd.wait()