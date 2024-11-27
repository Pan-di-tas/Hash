def buscar_clave(diccionario, clave):
    if clave in diccionario:
        return diccionario[clave]
    else:
        return "Clave no encontrada"

tabla_hash = {
    "id1": "Juan",
    "id2": "María",
    "id3": "Carlos"
}

clave = "id2"
resultado = buscar_clave(tabla_hash, clave)
print(f"Resultado de la búsqueda: {resultado}")
