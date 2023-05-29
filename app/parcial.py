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
        
   
        
#-----3)
def mostrar_logros():
    """muestra por consola los logros de un jugador elegido por el usuario"""
    while True:
        nombre = input("ingrese el nombre del jugador que desea buscar: ")
        if re.match("^([a-zA-Z]+)$",nombre):   
            posibles_jugadores = []
            for jugador in dream_team:
                if re.search(f"{nombre}", jugador["nombre"],re.IGNORECASE):
                    dato = {}
                    dato["nombre"] = jugador["nombre"]
                    dato["estadisticas"] = ", ".join(jugador["logros"])
                    posibles_jugadores.append(dato)
            return posibles_jugadores
        else:
            print("solo se acepta texto...")
    
    

#----4)
# Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
def calcular_promedio_total(opcion:bool,dato:str):
    """ si opcion es true , devuelve el promedio del dato que necesito por parametro sacando al peor en esa estadistica
    de lo contrario retornara el promedio total"""
    copia = copy.deepcopy(dream_team)
    acumulador = 0
    contador = 0
    if opcion == True:
        jugador_a_borrar = mostrar_jugadores_maximos(dato,"minimo")
        for jugador in copia:
            if jugador_a_borrar["nombre"] in jugador["nombre"]:
                copia.remove(jugador)
                break
    for jugador in copia:
        acumulador += jugador["estadisticas"][dato]
        contador += 1
    promedio = acumulador / contador
    return promedio
