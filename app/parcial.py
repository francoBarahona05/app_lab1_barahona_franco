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
            print("solo se acepta texto....")
    
#--------------------------------------------------------------------    
def obtener_estadistica_puntual(orden:str)->list:
    """con esta funcion obtengo el nombre y un dato especifico de las estadisticas que me van a servir en otros puntos
    del parcial para ser mas directo a la hora de mostrar el resultado y poder usar mas funciones devuelve una lista con diccionarios donde tengo nombre y estadistica puntual de los jugadores"""
    datos = []
    for jugadores in dream_team:
        dato = {
            "nombre" : jugadores["nombre"],
            orden : jugadores["estadisticas"]["{0}".format(orden)]
            }
        datos.append(dato)
    return datos


def ordenar_objeto(objeto:list[dict],clave:str,orden:str)->list[dict]:
    """" devuelve una lista ordenada de un diccionario con el formato de  "obtener_estadistica_puntual
    con estas 2 funciones muestro una lista ordenada de cualquier estadistica de cualquier jugador del dream team
    de forma acendente o decendente , recibiendo un objeto con una lista , una clave que quiero comparar y un tercer parametro donde aclaro si es de forma acendente o decendente"""
    
    if len(objeto) <= 1:
        return objeto
    else:
        pivote = objeto[0][clave]
        lista_uno = []
        lista_dos = []
        for jugador in objeto[1:]:
            if re.match("^acendente$",orden,re.IGNORECASE):
                if pivote >= jugador[clave]:
                    lista_uno.append(jugador)
                elif pivote <= jugador[clave]:
                    lista_dos.append(jugador)
            else:
                if pivote <= jugador[clave]:
                    lista_uno.append(jugador)
                elif pivote >= jugador[clave]:
                    lista_dos.append(jugador)
    lista_uno = ordenar_objeto(lista_uno,clave,orden)
    lista_uno.append(objeto[0])
    lista_dos = ordenar_objeto(lista_dos,clave,orden)
    lista_uno.extend(lista_dos)
    return lista_uno
#---------------------------------------------------------------------------------------------
#----4)

def mostrar_jugadores_maximos(clave:str,orden:str)->dict:
    """devuelve el mejor jugador con la clave que busquemos del dream team , devuelve maximos y minimos (puntos 4/7/8/9/15)"""
    referencia = dream_team[0]
    lista = []
    for jugador in dream_team[1:]:
        if re.match("^maximo$",orden,re.IGNORECASE):
            if referencia["estadisticas"][clave] <= jugador["estadisticas"][clave]:
                prospecto = {"nombre": jugador["nombre"],
                    f"{clave}" : jugador["estadisticas"][clave]
                }
                referencia = jugador
                lista.append(prospecto)

        elif re.match("^minimo$",orden,re.IGNORECASE):
            if referencia["estadisticas"][clave] >= jugador["estadisticas"][clave]:
                prospecto = {"nombre": jugador["nombre"],
                    f"{clave}" : jugador["estadisticas"][clave]
                }
                referencia = jugador
                lista.append(prospecto)
    return lista


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



# Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
def validar_jugador()->list:
    """valida si un jugador es miembro del salon de la fama"""
    while True:
        ingreso = input("ingrese el nombre exacto del jugador: ")
        for jugador in dream_team:
            if re.match("^{0}$".format(ingreso), jugador["nombre"],re.IGNORECASE):
                if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                    return print("es miembro del salon de la fama")
                    
                else:
                    return print("no es miembro del salon de la fama")
                
        print("el nombre ingresado esta mal escrito o no forma parte del dream team")
        
        
# 7) 8) 9)  Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.

def mostrar_jugadores_maximos(clave:str,orden:str)->dict:
    """devuelve el mejor jugador con la clave que busquemos del dream team , devuelve maximos y minimos (puntos 7/8/9/15/18)"""
    referencia = dream_team[11]
    maximo = None
    for jugador in dream_team:
        if re.match("^maximo$",orden,re.IGNORECASE):
            if referencia["estadisticas"][clave] < jugador["estadisticas"][clave]:
                prospecto = {"nombre": jugador["nombre"],
                    f"{clave}" : jugador["estadisticas"][clave]
                }
                referencia = jugador
                maximo = prospecto

        elif re.match("^minimo$",orden,re.IGNORECASE):
            if referencia["estadisticas"][clave] > jugador["estadisticas"][clave]:
                prospecto = {"nombre": jugador["nombre"],
                    f"{clave}" : jugador["estadisticas"][clave]
                }
                referencia = jugador
                maximo = prospecto
    return maximo



# Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
def mejores_que_el_promedio(clave:str)->list:
    """compara el dato ingresado y devuelve una lista con todos los que superen tal dato (punto 10/11/12/15/18)"""
    while True:  
        ingreso = input("ingrese un promedio para compara con los demas jugadores: ")
        jugadores_a_mostrar = []
        if re.match(r'^[-+]?\d*\.?\d+$', ingreso):
            for jugador in dream_team:
                if float(ingreso) < jugador["estadisticas"][clave]:
                    objeto = {
                        "nombre" : jugador["nombre"],
                        f"{clave}".replace("_"," ") : jugador["estadisticas"][clave]
                    }
                    jugadores_a_mostrar.append(objeto)
                else:
                    return print("el numero ingresado es muy alto")
            return jugadores_a_mostrar
        
        
def jugador_con_mas_logros()->dict:
    """retorna un diccionario con el jugador con mas logros obtenidos del dream team"""
    maximo = dream_team[0]
    for jugador in dream_team[1:]:
        if len(jugador["logros"]) > len(maximo["logros"]):
            maximo = jugador
    return maximo