"""
Realiza los siguientes cambios:
Cambia el valor 3 en matriz por 6.
Cambia el nombre del primer cantante por "Enrique Martin Morales".
En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".
En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
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
print("=" * 60)
print("Matriz original:", matriz)
print("=" * 60)
print("Cantantes original:", cantantes)
print("=" * 60)
print("Ciudades original:", ciudades)
print("=" * 60)
print("Coordenadas original:", coordenadas)
print("=" * 60)
print("<>" * 60)
print("=" * 60)

matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

print("Matriz:", matriz)
print("=" * 60)
print("Cantantes:", cantantes)
print("=" * 60)
print("Ciudades:", ciudades)
print("=" * 60)
print("Coordenadas:", coordenadas)