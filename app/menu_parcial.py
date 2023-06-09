from parcial import *
import re
def terminar_menu():    
    while True:
        pregunta = input("\n(ingrese un dato valido) desea  volver al menu principal?(no/si): ").lower()
        if re.match("^no$",pregunta):
            return True
        elif re.match("^si$",pregunta):
            return False

def dreeam_team_app() -> None:
    
    while True:
        menu =\
        """
        1 - Imprimir nombre y posición de los jugadores.
        2 - Imprimir las estadísticas del jugador seleccionado.
        3 - Buscar e imprimir logros de un jugador.
        4 - Imprimir promedio total de puntos por partido del Dream Team.
        5 - Consultar e imprimir si un jugador es miembro del Salón de la Fama de Baloncesto.
        6 - Imprimir jugador con la mayor cantidad de rebotes totales.
        7 - Imprimir jugador con el mayor porcentaje de tiros de campo.
        8 - Imprimir jugador con la mayor cantidad de asistencias totales.
        9 - Imprimir jugador con la mayor cantidad de robos totales.
        10 - ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
        11 - Imprimir jugadores con un promedio de puntos por partido superior a un valor dado.
        12 - Imprimir jugadores con un promedio de rebotes por partido superior a un valor dado.
        13 - Imprimir jugadores con un promedio de asistencias por partido superior a un valor dado.
        14 - Imprimir jugadores con un porcentaje de tiros libres superior a un valor dado.
        15 - Imprimir promedio de puntos por partido del equipo excluyendo al jugador con menos puntos por partido.
        16 - Imprimir jugador con la mayor cantidad de logros obtenidos.
        17 - Imprimir jugadores con un porcentaje de tiros triples superior a un valor dado.
        18 - Imprimir jugador con la mayor cantidad de temporadas jugadas.
        19 - Imprimir jugadores ordenados por posición con un porcentaje de tiros de campo superior a un valor dado.
        20 - Guardar las estadísticas de un jugador seleccionado en un archivo CSV.
        21 - Determinar la cantidad de jugadores que hay por cada posición.
        22 - Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente. 
        23 - Determinar qué jugador tiene las mejores estadísticas en cada valor
        24 - Determinar qué jugador tiene las mejores estadísticas de todos

        0 - Salir.

        _______________________________________________________________
        """

        
        opcion = None
        ingreso = input(f'{menu}Su opcion: ')
        
        if re.match('^[0-9]{1,2}$', ingreso):
            opcion = int(ingreso)
        else:
            if terminar_menu():
                break
            
        match opcion:
    
            case 1:
                mostrar_Datos( mostrar_jugadores())
                if terminar_menu():
                    break
            case 2:
                jugador = selecionar_jug_por_indice()
                mostrar_Datos(jugador)
                while True:
                    pregunta = input("usted desea pasar esta informacion a un archivo CSV?: ")
                    if re.match("^si$",pregunta,re.IGNORECASE):
                        guardar_estadisticas_csv(jugador)
                        break
                    elif re.match("^no$",pregunta,re.IGNORECASE):
                        break
                if terminar_menu():
                    break
            case 3:
                logros = mostrar_logros()
                mostrar_Datos(logros)
                if terminar_menu():
                    break
            case 4:
                # Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. 
                promedio = calcular_promedio_total(False,"promedio_puntos_por_partido")
                datos = obtener_estadistica_puntual("promedio_puntos_por_partido")
                datos_ordenados = ordenar_objeto(datos,"nombre","acendente")
                mostrar_Datos(datos_ordenados)
                print(f"el promedio total de todos los jugadores es: {round(promedio,2)}")
                if terminar_menu():
                    break
            case 5:
                # Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
                validar_jugador()
                if terminar_menu():
                    break
            case 6:
                # Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
                jugador_con_mas_rebotes = mostrar_jugadores_maximos("rebotes_totales","maximo")
                mostrar_Datos(jugador_con_mas_rebotes)
                if terminar_menu():
                    break
            case 7:
                jugador_con_mas_porcentaje_tir_campo = mostrar_jugadores_maximos("porcentaje_tiros_de_campo","maximo")
                mostrar_Datos(jugador_con_mas_porcentaje_tir_campo)
                if terminar_menu():
                    break
            case 8:
                jugador_con_mas_asistencias_totales = mostrar_jugadores_maximos("asistencias_totales","maximo")
                mostrar_Datos(jugador_con_mas_asistencias_totales)
                
                if terminar_menu():
                    break            
            case 9:
                mejores = mejores_que_el_promedio("promedio_puntos_por_partido")
                mostrar_Datos(mejores)
                if terminar_menu():
                    break
            case 10:
                mejores = mejores_que_el_promedio("promedio_rebotes_por_partido")
                mostrar_Datos(mejores)
                if terminar_menu():
                    break
            case 11:
                mejores = mejores_que_el_promedio("promedio_asistencias_por_partido")
                mostrar_Datos(mejores)
                if terminar_menu():
                    break   
            case 12:
                # Calcular y mostrar el jugador con la mayor cantidad de robos totales.
                jugador_con_mas_porcentaje_tir_campo = mostrar_jugadores_maximos("robos_totales","maximo")
                mostrar_Datos(jugador_con_mas_porcentaje_tir_campo)
                if terminar_menu():
                    break

            case 13:
                # Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
                jugador_con_mas_porcentaje_tir_campo = mostrar_jugadores_maximos("bloqueos_totales","maximo")
                mostrar_Datos(jugador_con_mas_porcentaje_tir_campo)
                if terminar_menu():
                    break
            case 14:
                # Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
                mejores = mejores_que_el_promedio("porcentaje_tiros_libres")
                mostrar_Datos(mejores)
                if terminar_menu():
                    break   
            case 15:
                # Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
                promedio_sin_el_peor_jug = calcular_promedio_total(True,"promedio_puntos_por_partido")
                print(f"el promedio total de puntos  por partidos del dream team sacando al peor jugador en cuanto a tal estadistica es: {round(promedio_sin_el_peor_jug,2)}")
                if terminar_menu():
                    break
            case 16:
                # Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
                jug_mas_logros = jugador_con_mas_logros()
                mostrar_Datos(jug_mas_logros)
                if terminar_menu():
                    break                

            case 17:
                # Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
                mejores = mejores_que_el_promedio("porcentaje_tiros_triples")
                mostrar_Datos(mejores)
                if terminar_menu():
                    break
            case 18:
                # Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas
                jugador_con_mas_temporadas = mostrar_jugadores_maximos("temporadas","maximo")
                mostrar_Datos(jugador_con_mas_temporadas)
                if terminar_menu():
                    break

            case 19:
                # Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
                jugadores_ordenados = mostrar_jugadores_por_posicion()
                mostrar_Datos(jugadores_ordenados)
                if terminar_menu():
                    break
            case 20:
                jugadores23 = BONUS()
                mostrar_Datos(jugadores23)
                csv_23(jugadores23)
                if terminar_menu():
                    break
            case 21: 
                respuesta = determinar_cant_posiciones()
                mostrar_Datos(respuesta)
                if terminar_menu():
                    break
            case 22:
                all_star = jugadores_all_star()
                mostrar_Datos(all_star)
                if terminar_menu():
                    break
            case 23:
                mejores_estadisticas = maximo_segun_estadisticas()
                mostrar_Datos(mejores_estadisticas)
                if terminar_menu():
                    break
            case 24:
                encontrar_mejor_jugador_mejor_estadistica(dream_team)
                if terminar_menu():
                    break
            case 0 :
                break
            case _:
                print(f'La opcion {opcion} es incorrecta!', 'error')               
dreeam_team_app()
