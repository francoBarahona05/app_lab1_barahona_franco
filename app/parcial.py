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
    """retorna una lista de diccionarios con nombre y la posicion de los jugadores del equipo"""
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
def obtener_estadistica_puntual(clave:str)->list:
    """con esta funcion obtengo el nombre y un dato especifico de las estadisticas que me van a servir en otros puntos
    del parcial para ser mas directo a la hora de mostrar el resultado y poder usar mas funciones devuelve una lista con diccionarios donde tengo nombre y estadistica puntual de los jugadores"""
    datos = []
    for jugadores in dream_team:
        dato = {
            "nombre" : jugadores["nombre"],
            clave : jugadores["estadisticas"]["{0}".format(clave)]
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

def mostrar_jugadores_maximos(clave:str,tipo:str)->dict:                
    """Devuelve el mejor jugador con la clave que busquemos del dream team, devuelve máximo (puntos 7/8/9/19)"""
    
    maximo = {
        "nombre": dream_team[0]["nombre"],
        clave.replace("_", " "): dream_team[0]["estadisticas"].get(clave, 0)
    }
    
    for jugador in dream_team:
        valor_actual = jugador["estadisticas"].get(clave, 0)
        
        if re.search("^maximo$", tipo, re.IGNORECASE):
            if valor_actual > maximo[clave.replace("_", " ")]:
                maximo[clave.replace("_", " ")] = valor_actual
                maximo["nombre"] = jugador["nombre"]
        elif re.search("^minimo$", tipo, re.IGNORECASE):
            if valor_actual < maximo[clave.replace("_", " ")]:
                maximo[clave.replace("_", " ")] = valor_actual
                maximo["nombre"] = jugador["nombre"]
    
    return maximo
 

# Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
def calcular_promedio_total(opcion:bool,dato:str):
    """ si opcion es true , devuelve el promedio del dato que necesito por parametro sacando al peor en esa estadistica
    de lo contrario retornara el promedio total"""
    copia = copy.deepcopy(dream_team)
    acumulador = 0
    contador = 0
    if opcion == True:
        jugador_a_borrar = mostrar_jugadores_maximos("promedio_puntos_por_partido","minimo")
        for jugador in copia:
            if jugador_a_borrar["nombre"] in jugador["nombre"]:
                copia.remove(jugador)
                break
    for jugador in copia:
        acumulador += jugador["estadisticas"][dato]
        contador += 1
    promedio = acumulador / contador
    return promedio


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
            return jugadores_a_mostrar
        
def jugador_con_mas_logros()->dict:
    """retorna un diccionario con el jugador con mas logros obtenidos del dream team"""
    maximo = dream_team[0]
    for jugador in dream_team[1:]:
        if len(jugador["logros"]) > len(maximo["logros"]):
            maximo = jugador
    logros = {"nombre":maximo["nombre"],"logros":" ,".join(maximo["logros"])}
    return logros
 
#20
def mostrar_jugadores_por_posicion():
    mejores = mejores_que_el_promedio("porcentaje_tiros_de_campo")
    for jugador in mejores:
        for jug_ in dream_team:
            if jugador["nombre"] == jug_["nombre"]:
                jugador["posicion"] = jug_["posicion"]
    mejores_ordenados = ordenar_objeto(mejores,"posicion","acendente")
    return mejores_ordenados

def BONUS():
    
    jugadores = {}
    estadisticas = ["puntos_totales","asistencias_totales","rebotes_totales","robos_totales"]
    for clave in estadisticas:
        puntos_sin_ordenar = obtener_estadistica_puntual(f"{clave}")
        puntos_ordenados = ordenar_objeto(puntos_sin_ordenar,f"{clave}","decendente")  
        for indice,jugador in enumerate(puntos_ordenados):
            jugador[f"ranking {clave}"] =  f"{indice + 1}"
        
        for jug in puntos_ordenados:
            if not jug["nombre"] in jugadores:
                jugadores[jug["nombre"]] = {f"{clave}": jug[f"ranking {clave}"]}
            else:
                jugadores[jug["nombre"]][f"{clave}"] = jug[f"ranking {clave}"]
    

    # puntos_sin_ordenar = obtener_estadistica_puntual("puntos_totales")
    # puntos_ordenados = ordenar_objeto(puntos_sin_ordenar,"puntos_totales","decendente")
    # for indice,jugador in enumerate(puntos_ordenados):
    #     jugador["ranking puntos"] = f"{indice + 1 }"  
    
    # asistencias_sin_ordenar = obtener_estadistica_puntual("asistencias_totales")
    # asistencias_ordenados = ordenar_objeto(asistencias_sin_ordenar,"asistencias_totales","decendente")
    # for indice,jugador in enumerate(asistencias_ordenados):
    #     jugador["ranking asistencias"] = f"{indice + 1 }" 
        
    # rebotes_sin_ordenar = obtener_estadistica_puntual("rebotes_totales")
    # rebotes_ordenados = ordenar_objeto(rebotes_sin_ordenar,"rebotes_totales","decendente")
    # for indice,jugador in enumerate(rebotes_ordenados):
    #     jugador["ranking rebotes"] = f"{indice + 1 }" 
        
    # robos_sin_ordenar = obtener_estadistica_puntual("robos_totales")
    # robos_ordenados = ordenar_objeto(robos_sin_ordenar,"robos_totales","decendente")
    # for indice,jugador in enumerate(robos_ordenados):
    #     jugador["ranking robos"] =  f"{indice + 1 }"   

    # jugadores = {}

    # for jug in puntos_ordenados:
        
    #     jugadores[jug["nombre"]] = { "rank puntos": jug["ranking puntos"]}

    # for jug in asistencias_ordenados:
   
    #     if  jug["nombre"] in jugadores:
    #         jugadores[jug["nombre"]]["rank asistencias"] = jug["ranking asistencias"]

    # for jug in rebotes_ordenados:
 
    #     if  jug["nombre"] in jugadores:
    #         jugadores[jug["nombre"]]["rank rebotes"] = jug["ranking rebotes"]

    # for jug in robos_ordenados:
 
    #     if jug["nombre"] in jugadores:
    #         jugadores[jug["nombre"]]["rank robos"] = jug["ranking robos"]

    return jugadores

def csv_23(jugadores_punto_23):
    nombres = jugadores_punto_23.keys()
    rankings = ["nombre de los jugadores", "puntos_totales","asistencias_totales","rebotes_totales","robos_totales"]
    # Abrir el archivo CSV en modo de escritura
    with open("app/tabla_rankings.csv", 'w',newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=".")
        encabezado = [f"{ranking:>20}" for ranking in rankings]
        writer.writerow(encabezado)

        # Escribir las filas con los datos de los jugadores
        for nombre in nombres:
            fila = [f"{nombre.ljust(19)}"]
            for ranking in rankings[1:]:
                fila.append(f"{jugadores_punto_23[nombre][ranking]:>20}")
            writer.writerow(fila)

#punto 21 Determinar la cantidad de jugadores que hay por cada posición.
def determinar_cant_posiciones():
    contadores = {
        "Base": 0,
        "Alero": 0,
        "Escolta": 0,
        "Ala-Pivot": 0,
        "Pivot": 0
    }

    for jugador in dream_team:
        posicion = jugador["posicion"]
        if posicion in contadores:
            contadores[posicion] += 1

    return contadores
# 22 Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente.
def jugadores_all_star():
    lista = []
    for jugador in dream_team:
        for logro in jugador["logros"]:
            if re.search("veces All-Star", logro):
                jugador_formateado = {}
                jugador_formateado["nombre"] = jugador["nombre"]
                all_star = re.findall(r'\d+', logro) 
                jugador_formateado["all star"] = int(all_star[0])  
                lista.append(jugador_formateado)
    lista_ordenada = ordenar_objeto(lista,"all star","decendente")
    return lista_ordenada

#23Determinar qué jugador tiene las mejores estadísticas en cada valor. La salida por pantalla
def maximo_segun_estadisticas() -> str:
    estadisticas_claves = dream_team[0]["estadisticas"].keys()
    mejores_estadisticas = []
    for clave in estadisticas_claves:
        jugador = {}
        max_estadisticas = mostrar_jugadores_maximos(clave,"maximo")
        jugador["nombre"] = max_estadisticas["nombre"]
        jugador[f"maximo en {clave}".replace("_"," ")] = max_estadisticas[f"{clave}".replace("_"," ")]
        mejores_estadisticas.append(jugador)
    return mejores_estadisticas


#24 Determinar qué jugador tiene las mejores estadísticas de todos.
def encontrar_mejor_jugador_mejor_estadistica(lista_jugadores):
    """
    Esta función encuentra al jugador con las mejores estadísticas generales de una lista de jugadores.
    """
    if len(lista_jugadores) > 0:
        max_puntaje = 0
        max_jugador = None

        for jugador in lista_jugadores:
            puntaje_total = sum(jugador["estadisticas"].values())
            if puntaje_total > max_puntaje:
                max_puntaje = puntaje_total
                max_jugador = jugador

        if max_jugador:
            print("El jugador con las mejores estadísticas es {0} con un total de {1} puntos totales.".format(max_jugador["nombre"], round(max_puntaje,2)))
        else:
            print("No se encontró ningún jugador en la lista.")
    else:
        print("Error, lista vacía!")

encontrar_mejor_jugador_mejor_estadistica(dream_team)