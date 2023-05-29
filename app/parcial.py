import re
import csv
import copy
import json


jugadores_por_indice_str =\
"""
nombre: Michael Jordan  opcion: 1
nombre: Magic Johnson  opcion: 2
nombre: Larry Bird  opcion: 3
nombre: Charles Barkley  opcion: 4
nombre: Scottie Pippen  opcion: 5
nombre: David Robinson  opcion: 6
nombre: Patrick Ewing  opcion: 7
nombre: Karl Malone  opcion: 8
nombre: John Stockton  opcion: 9
nombre: Clyde Drexler  opcion: 10
nombre: Chris Mullin  opcion: 11
nombre: Christian Laettner  opcion: 12

"""

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



#---------2)
def selecionar_jug_por_indice()->list:
    """devuelve una lista con el jugador elegido por el indice por le usuario"""
    while True:
        ingreso = input(f"{jugadores_por_indice_str}ingrese solo el numero de la  opcion del jugador que quiere ver sus estadisticas: ")

        if re.match("^(1[0-2]|[1-9])$",ingreso):
            datos = []
            dato = dream_team[int(ingreso)-1]["estadisticas"]
            for clave,valor in dato.items():
                texto = "{0} : {1}".format(clave,valor)
                datos.append(texto)
            return datos
        else:
            print("ingrese un dato valido (1 al 12)")
            
def guardar_estadisticas_csv(dato:list):
    """guarda las estadisticas de un jugador"""
    with open("app/estadisticas.csv","w") as archivo:
        for i in dato:
            archivo.write("{0}\n".format(i))
    print("archivo creado!")
        