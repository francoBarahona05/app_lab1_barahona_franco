import re
import csv
import copy
import json


def leer_archivo_json()->list:
    """devuelve una lista del archivo json de datos"""
    with open("app/dt.json","r",encoding="utf-8") as archivo:
        dato = json.load(archivo)
    return dato["jugadores"]
dream_team = leer_archivo_json()

# 1) Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta

def mostrar_jugadores()->list:
    """retorna una lista de diccionarios con nombre e informacion de los jugadores del equipo"""
    jugadores = []
    for jugador in dream_team:
        dato = "nombre: {0}  posicion: {1}".format(jugador["nombre"],jugador["posicion"])
        jugadores.append(dato)
    return jugadores
    
def mostrar_Datos(dato):
    """funcion que prepare para mostrar los datos"""
    if isinstance(dato,list):
        for i in  dato : 
            if isinstance(i,dict):
                dato = [f"{clave} : {valor}" for clave,valor in i.items()]
                print(",      ".join(dato))
            elif isinstance(i,str):
                print(i)
    elif isinstance(dato,dict):
        dato_uno = [f"{clave} : {valor}"for clave,valor in dato.items()]
        print("\n".join(dato_uno))
    else:
        print("dato no admitido")


