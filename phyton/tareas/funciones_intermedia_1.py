# Datos originales
matriz = [[10, 15, 20], [3, 7, 14]]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "Tata Barahona", "pais": "Chile"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Actualización de valores
matriz[1][0] = 6  # 3 por 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# Def - funciones

def iterarDiccionario(lista):
    for elemento in lista:
        for clave, valor in elemento.items():
            print(f"{clave}: {valor}")
        print("---"*60)

def iterarDiccionario2(llave, lista):
    for elemento in lista:
        valor = elemento.get(llave, "Llave no encontrada")
        print(f"{llave}: {valor}")

def imprimirInformacion(diccionario):
    """
    Imprime la clave y los elementos de la lista asociada dentro del diccionario.
    """
    for clave, valor in diccionario.items():
        print(f"{clave.upper()} ({len(clave)} caracteres):")
        for item in valor:
            print(f" - {item}")
        print()

# Datos para pruebas
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# Ejecución de funciones
print("Iteración completa de cantantes:")
iterarDiccionario(cantantes)

print("\nIteración parcial ('nombre'):")
iterarDiccionario2("nombre", cantantes)

print("\nInformación sobre Costa Rica:")
imprimirInformacion(costa_rica)