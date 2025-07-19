import tkinter as tk
import numpy as np
import sounddevice as sd

# Parámetros generales
amplitud = 0.5
duracion = 0.5
tasa_muestreo = 44100
nota_base = 440  # La4

# Cálculo de frecuencia por semitono
def obtener_frecuencia(semitonos):
    return nota_base * (2 ** (semitonos / 12))

# Función para reproducir la nota
def reproducir_nota(semitonos):
    frecuencia = obtener_frecuencia(semitonos)
    t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False)
    tono = amplitud * np.sin(2 * np.pi * frecuencia * t)
    sd.play(tono, tasa_muestreo)
    sd.wait()

# Crear ventana
ventana = tk.Tk()
ventana.title("Teclado Virtual")

# Notas de la escala mayor (La mayor)
notas = {
    "La": 0, "Si": 2, "Do#": 4, "Re": 5,
    "Mi": 7, "Fa#": 9, "Sol#": 11, "La5": 12
}

# Crear botones
for nombre, semitonos in notas.items():
    boton = tk.Button(
        ventana,
        text=nombre,
        width=10,
        height=3,
        command=lambda s=semitonos: reproducir_nota(s)
    )
    boton.pack(side=tk.LEFT, padx=5, pady=10)

ventana.mainloop()