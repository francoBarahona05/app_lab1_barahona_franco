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
        10 - Imprimir jugador con la mayor cantidad de bloqueos totales.
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
        23 - BONUS!
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
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                pass
            case 20:
                pass
            case 0 :
                break
            case _:
                print(f'La opcion {opcion} es incorrecta!', 'error')               
        
dreeam_team_app()
