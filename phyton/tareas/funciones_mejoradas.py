import tkinter as tk
from tkinter import messagebox


def mostrar_horarios_disponibles(citas, fecha, horarios_posibles):
    ocupados = [cita['horario'] for cita in citas if cita['fecha'] == fecha]
    return [h for h in horarios_posibles if h not in ocupados]

def verificar_disponibilidad(citas, fecha, horario):
    return all(cita['fecha'] != fecha or cita['horario'] != horario for cita in citas)

def registrar_cita(citas, historial, id, nombre, fecha, motivo, tutor, horario):
    nueva = {
        'id': id, 'nombre': nombre, 'fecha': fecha,
        'motivo': motivo, 'tutor': tutor, 'horario': horario
    }
    citas.append(nueva)
    historial.setdefault(id, []).append(nueva)

def mostrar_historial(historial, id_mascota):
    if id_mascota in historial:
        return "\n".join([
            f"{cita['fecha']} - {cita['motivo']} - {cita['horario']}" 
            for cita in historial[id_mascota]
        ])
    return "Sin historial disponible."

def mostrar_citas_del_dia(citas, fecha):
    filtradas = [c for c in citas if c['fecha'] == fecha]
    if filtradas:
        return "\n".join([
            f"{c['nombre']} ({c['id']}) - {c['horario']} - {c['motivo']}"
            for c in filtradas
        ])
    return "No hay citas para esa fecha."

def cancelar_cita(citas, historial, id_mascota, fecha, horario):
    citas[:] = [c for c in citas if not (
        c['id'] == id_mascota and c['fecha'] == fecha and c['horario'] == horario
    )]
    if id_mascota in historial:
        historial[id_mascota] = [
            c for c in historial[id_mascota]
            if not (c['fecha'] == fecha and c['horario'] == horario)
        ]

# Datos
citas = []
historial = {}
horarios_posibles = ["10:00", "11:00", "12:00", "13:00"]

# Interfaz
ventana = tk.Tk()
ventana.title("VetCare - Gestión de Citas")
ventana.geometry("550x600")
ventana.configure(bg="#f2f2f2")

frame_mascota = tk.LabelFrame(ventana, text="Datos de la Mascota", padx=10, pady=10, bg="#f2f2f2")
frame_mascota.pack(padx=10, pady=5, fill="x")

frame_cita = tk.LabelFrame(ventana, text="Datos de la Cita", padx=10, pady=10, bg="#f2f2f2")
frame_cita.pack(padx=10, pady=5, fill="x")

frame_botones = tk.Frame(ventana, bg="#f2f2f2")
frame_botones.pack(padx=10, pady=10, fill="x")

def campo(frame, label):
    tk.Label(frame, text=label, bg="#f2f2f2").pack(anchor="w")
    entrada = tk.Entry(frame)
    entrada.pack(fill="x")
    return entrada

entry_id = campo(frame_mascota, "ID Mascota")
entry_nombre = campo(frame_mascota, "Nombre Mascota")
entry_tutor = campo(frame_mascota, "Nombre del Tutor")

entry_fecha = campo(frame_cita, "Fecha (dd/mm/yy)")
entry_motivo = campo(frame_cita, "Motivo de la cita")

tk.Label(frame_cita, text="Horario", bg="#f2f2f2").pack(anchor="w")
horario_var = tk.StringVar()
horario_var.set(horarios_posibles[0])
entry_horario = tk.OptionMenu(frame_cita, horario_var, *horarios_posibles)
entry_horario.pack(fill="x")

def registrar():
    id = entry_id.get()
    nombre = entry_nombre.get()
    fecha = entry_fecha.get()
    motivo = entry_motivo.get()
    tutor = entry_tutor.get()
    horario = horario_var.get()

    if not verificar_disponibilidad(citas, fecha, horario):
        messagebox.showerror("Horario ocupado", "Ese horario ya fue reservado.")
        return

    registrar_cita(citas, historial, id, nombre, fecha, motivo, tutor, horario)
    messagebox.showinfo("Éxito", f"Cita registrada para {nombre} el {fecha} a las {horario}.")
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_motivo.delete(0, tk.END)
    entry_tutor.delete(0, tk.END)
    horario_var.set(horarios_posibles[0])

def ver_horarios():
    fecha = entry_fecha.get()
    disponibles = mostrar_horarios_disponibles(citas, fecha, horarios_posibles)
    if disponibles:
        messagebox.showinfo("Horarios disponibles", "\n".join(disponibles))
    else:
        messagebox.showwarning("Sin disponibilidad", "No hay horarios para esa fecha.")

def ver_historial():
    id = entry_id.get()
    texto = mostrar_historial(historial, id)
    messagebox.showinfo("Historial de citas", texto)

def ver_citas():
    fecha = entry_fecha.get()
    texto = mostrar_citas_del_dia(citas, fecha)
    messagebox.showinfo("Citas del día", texto)

def cancelar():
    id = entry_id.get()
    fecha = entry_fecha.get()
    horario = horario_var.get()
    cancelar_cita(citas, historial, id, fecha, horario)
    messagebox.showinfo("Cancelación", "Cita cancelada correctamente.")

botones = [
    ("Registrar Cita", registrar),  
    ("Ver Horarios Disponibles", ver_horarios),
    ("Ver Historial de Citas", ver_historial),
    ("Ver Citas del Día", ver_citas),
    ("Cancelar Cita", cancelar)
]
for texto, comando in botones:
    btn = tk.Button(frame_botones, text=texto, command=comando, bg="#4CAF50", fg="white")
    btn.pack(side="left", padx=5, pady=5, expand=True, fill="x")

ventana.mainloop()