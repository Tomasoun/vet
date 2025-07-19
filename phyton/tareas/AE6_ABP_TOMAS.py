"""
Crea el archivo un Python llamado funciones_intermedias_1.py
Actualiza los valores en diccionarios y listas
Crea la función iterarDiccionario(lista)
Crea la función iterarDiccionario2(llave, lista)
Crea la función imprimirInformacion(diccionario)
"""
"""
Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
En ciudades, cambia “Cancún” por “Monterrey”
En las coordenadas, cambia el valor de “latitud” por 9.9355431
"""
matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(lista):
    for elemento in lista:
        print(elemento)

def iterarDiccionario2(llave, lista):
    for elemento in lista:
        if llave in elemento:
            print(f"{llave}: {elemento[llave]}")
iterarDiccionario(cantantes)
iterarDiccionario2("nombre", cantantes)
def imprimirInformacion(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave, valor in costa_rica.items():
    print(len(clave), (valor.upper()))
    for i in valor:
        print(i)
        
      