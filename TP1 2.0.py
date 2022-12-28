import random


DICCSERPIENTES: dict = {86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}
DICCESCALERAS: dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96}


def menu() -> None:
    print("        =============================================================================="
          "\n               ||                     M E N U                             ||"
          "\n        ==============================================================================")
    print("\n"
          "\t1) INICIAR PARTIDA\n"
          "\t2) ESTADISTICAS\n"
          "\t3) RESETEAR ESTADISTICAS\n"
          "\t4) FINALIZAR PARTIDA\n")
    print()


def bienvenida() -> None:
    print("       ==============================================================================="
          "\n         ||                     ¡BIENVENIDO AL JUEGO!                             ||"
          "\n       ===============================================================================")
    print()


def despedida() -> None:
    print("        ==============================================================================="
          "\n           ||                     ¡HASTA LA PRÓXIMA!                             ||"
          "\n        ===============================================================================")
    print()


def crear_tablero() -> list:
    """
    > Crea un tablero con los valores del 1 al 10
    """
    tablero: list = []
    n: int = 100
    for i in range(10):
        tablero.append([])
        if n % 10 == 0:
            for j in range(n, n - 10, - 1):
                tablero[i].append(j)
            n -= 19
        elif n % 10 != 0:
            for j in range(n, n + 10, + 1):
                tablero[i].append(j)
            n -= 1

    return tablero


def validar_opcion_modificacion(mensaje_input: str, mensaje_error: str, op_min: int, op_max: int) -> int:
    """
    > Recibe mensajes de input y error, el tope inferior y el superior.
    > Retorna la opcion validada por el usuario
    """
    respuesta = input(mensaje_input)

    while(not respuesta.isnumeric() or int(respuesta) > op_max or int(respuesta) < op_min):
        print(mensaje_error)
        respuesta = input(mensaje_input)
    return int(respuesta)


def ingresar_jugadores() -> dict:
    """
    > Recibe la cantidad de nuevos jugadores especificada por parametro
    > Retorna un diccionario que contiente una lista > [J1, nombre_jugador, posicion, turno]
    """
    jugadores: dict = {}
    posicion: int = 1
    cant_jugadores: int = 2
    nro_jugador: int = 0
    turno: int = 0

    while nro_jugador != cant_jugadores:
        jugador: str = input("|||  INGRESE EL NOMBRE DEL JUGADOR >  ").upper()
        nro_jugador += 1
        jnro: str = f"J{nro_jugador}"
        jugadores[nro_jugador] = [jnro, jugador, posicion, turno]

    return jugadores


def modificar_turno(jugadores: dict, turno: int) -> int:
    """
    > Teniendo en cuenta la cantidad de jugadores > va modificando el turno
    > En caso de que recien se haya iniciado la partida (turno = 0) > el programa elige aleatoriamente
      entre los jugadores quien comenzara
    """
    cantidad_jugadores: int = len(jugadores)

    if turno == 0:
        turno: int = random.randint(1, cantidad_jugadores)
    elif turno == 1:
        turno += 1
    elif turno == 2:
        turno -= 1

    return turno


def tirar_dado(op: int) -> int:
    """
    (tirar_dado) > emula un dado de 6 caras
    > Al ingresar cualquier numero > nos devuelve un numero aleatorio del 1 al 6
    """
    nro: int = 0
    if op == 1:
        nro: int = random.randint(1, 7)
    print(f"||| CONSEGUISTE UN > {nro}")

    return nro


def modificar_posicion(jugadores: dict, dado: int, turno: int) -> int:
    """
    >Toma la posicion actual del jugador(ubi)
    >Suma la posicion al valor del dado obtenido
    >Resultado de la suma > nueva posicion obtenida

    """
    nueva_posicion: int = jugadores[turno][2] + dado

    return nueva_posicion


def cascara_banana(posicion: int) -> int:

    """
    > Si la posicion esta en el casillero CASCARA DE BANANA, el jugador cae dos pisos.
    > Si posicion = 76 -> nueva posicion = 56

    """
    nueva_posicion: int = 0

    nueva_posicion = posicion - 20

    return nueva_posicion


def magico(posicion: int) -> int:
    """
    > Si la posicion esta en el casillero MAGICO > el jugador puede caer en cualquier otro casillero
    > Restriccion: no se puede transportar al 1 o al 100

    """
    nueva_posicion: int = random.randint(2, 99)

    return nueva_posicion


def rushero(posicion: int) -> int:
    """
     > Si la posicion esta en el casillero RUSHERO
     > El jugador corre hasta la esquina de la parte ASCENDENTE del tablero
     > Si posicion = 16 -> nueva posicion = 20

    """
    tablero: list = crear_tablero()
    nueva_posicion: int = 0

    for i in tablero:
        if posicion in i:
            if posicion >= i[0]:
                nueva_posicion = i[9]
            elif posicion <= i[0]:
                nueva_posicion = i[0]
    return nueva_posicion


def hongos_locos(posicion: int) -> int:
    """
    > Si la posicion esta en el casillero HONGOS LOCOS
    > El jugador corre hasta la esquina de la parte DESCENDENTE del tablero
    > Si posicion = 84 -> nueva posicion = 81

    """
    tablero: list = crear_tablero()
    nueva_posicion: int = 0

    for i in tablero:
        if posicion in i:
            if posicion >= i[0]:
                nueva_posicion = i[9]
            elif posicion <= i[0]:
                nueva_posicion = i[0]
    return nueva_posicion


    return nueva_posicion


def serp_esca(posicion: int) -> int:
    """
    > Busca en su respectivo diccionario si la posicion se encuentra en una SERPIENTE o ESCALERA
    > De ser que si > nos devuelve la nueva posicion
    > En caso contrario > nos devuelve 0

    """
    nueva_posicion: int = 0
    if posicion in DICCESCALERAS.keys():
        nueva_posicion = DICCESCALERAS[posicion]
        print("\t|||HA CAIDO EN UNA ESCALERA|||\t")

    elif posicion in DICCSERPIENTES.keys():
        nueva_posicion = DICCSERPIENTES[posicion]
        print("\t|||HA CAIDO EN UNA SERPIENTE|||\t")

    else:
        nueva_posicion = 0

    return nueva_posicion


def random_casilleros() -> list:
    """
    > Toma posiciones aleatorias del tablero y se las atribuye a los diferentes casilleros especiales
    > Las posiciones son almacenadas en la lista del respectivo casillero especial
    > C/ lista de los casilleros especiales es almacenada en una lista general(return)
    > RESTRICIONES:
      -Cascara de banana > debe ser un casillero a partir del 21 (inclusive) en adelante
                         > cant casilleros : 5
      -Rushero > no puede colocarse en el MAX nro de c/ piso
               > cant casilleros: 1
      -Hongos Locos > no puede colocarse en el MIN nro de c/ piso
                    > cant casilleros: 1
      -Magico > cant casilleros: 3
      -No deben repetirse, ni superpornerse con con la cabeza o cola de la serpiente (igual para las escaleras)

    """

    tablero: list = crear_tablero()
    cb: list[int] = []
    mg: list[int] = []
    ru: list[int] = []
    hl: list[int] = []
    cond_rushero: list[int] = []
    cond_hlocos: list[int] = []
    casilleros_esp: list[list[int]] = [cb, mg, ru, hl]
    condicion: bool = True

    for i in tablero:
        for j in i:
            if (j == i[0] and j > i[9]) or (j == i[9] and j > i[0]):
                    cond_rushero.append(j)
            elif (j == i[0] and j < i[9]) or (j == i[9] and j < i[0]):
                    cond_hlocos.append(j)
    # Ambas listas estan formadas por los casilleros en los cuales no se puede encontrar el rushero o el
    # de hongos locos

    while condicion is True:
        randomizador: int = random.randint(2, 99)

        if randomizador not in DICCSERPIENTES.keys() and randomizador not in DICCSERPIENTES.values() and \
                randomizador not in DICCESCALERAS.keys() and randomizador not in DICCESCALERAS.values():

            if len(cb) < 5 and randomizador in range(21, 100):
                cb.append(randomizador)
            elif len(mg) < 3 and randomizador not in cb:
                mg.append(randomizador)
            elif randomizador not in cb and randomizador not in mg:
                if len(ru) < 1 and randomizador not in cond_rushero:
                    ru.append(randomizador)
                elif len(hl) < 1 and randomizador not in cond_hlocos and randomizador not in ru:
                    hl.append(randomizador)
            else:
                condicion = False

    return casilleros_esp


def tablero_casillerosesp(casilleros_esp: list) -> list:
    """
    > Teniendo en cuenta la lista "casilleros_especiales" y los diccionarios(serpientes y escaleras) que contienen
      valores del tipo entero, que me marcan donde se encuentran tales casilleros.
    > Retorna el tablero modificado, especificando con sus iniciales correspondientes donde estan los casilleros
      especiales

    """
    tablero: list = crear_tablero()

    for i in tablero:
        for j in range(len(i)):
            if i[j] in casilleros_esp[0]:
                i[j] = "CB"
            elif i[j] in casilleros_esp[1]:
                i[j] = "MA"
            elif i[j] in casilleros_esp[2]:
                i[j] = "RU"
            elif i[j] in casilleros_esp[3]:
                i[j] = "HL"
            elif i[j] in DICCESCALERAS.keys():
                i[j] = "E"
            elif i[j] in DICCSERPIENTES.keys():
                i[j] = "S"

    return tablero


def posicion_en_tablero(tablero: list, jugadores: dict, casilleros_esp: list) -> None:
    """
    > Sigue la posicion del jugador en el tablero y lo modifica de acuerdo a su ubicacion
    """
    posicion_j1: int = jugadores[1][2]
    posicion_j2: int = jugadores[2][2]
    jugador1: str = jugadores[1][0]
    jugador2: str = jugadores[2][0]
    casilleros_especiales: list = casilleros_esp

    for lista in tablero:
        for valor in range(len(lista)):
            if lista[valor] == posicion_j1:
                lista[valor] = jugador1
            if lista[valor] == posicion_j2:
                lista[valor] = jugador2
    imprimir_tablero(tablero)


def imprimir_tablero(tablero: list) -> None:
    """
    > Procedimiento que me imprime el tablero con sus modificaciones correspondientes
    """
    for i in tablero:
        for j in i:
            print(j, end="\t|")

        print(end='\n')


def modificar_estadisticas(estadisticas: list, casilleros_esp: list, jugadores_posicion: int) -> list:
    """
    > Toma la lista estadisticas y en caso de haber caido en un casillero especial la modifica
    > Retorna la lista actualizada
    """

    posicion: int = jugadores_posicion

    if posicion in casilleros_esp[0]:
        estadisticas[0] += 1
    elif posicion in casilleros_esp[1]:
        estadisticas[1] += 1
    elif posicion in casilleros_esp[2]:
        estadisticas[2] += 1
    elif posicion in casilleros_esp[3]:
        estadisticas[3] += 1
    elif posicion in DICCESCALERAS.keys():
        estadisticas[4] += 1
    elif posicion in DICCSERPIENTES.keys():
        estadisticas[5] += 1

    return estadisticas


def casilleros_posicion(posicion: int, casilleros_esp: list, estadisticas: list) -> int:

    """
    > Toma la posicion ya modificada (modificar_posicion)
    > Toma la lista general de los casilleros especiales (random_casilleros)
    > Teniendo en cuenta que la lista casilleros_esp tiene atribuido a c\ indice una lista:
      - 0 -> lista casilleros cascara de banana
      - 1 -> lista casilleros magico
      - 2 -> lista casillero rushero
      - 3 -> lista casillero hongos locos
    > Si la posicion se encuentra en alguna de las listas -> llama a la funcion correspondiente
    > Devuelve la nueva poscion
    """

    nueva_posicion: int = 0

    if posicion in casilleros_esp[0]:
        nueva_posicion = cascara_banana(posicion)
        print("\t|||HA CAIDO EN EL CASILLERO CASCARA DE BANANA|||\t")
    elif posicion in casilleros_esp[1]:
        nueva_posicion = magico(posicion)
        print("\t|||HA CAIDO EN EL CASILLERO MAGICO|||\t")
    elif posicion in casilleros_esp[2]:
        nueva_posicion = rushero(posicion)
        print("\t|||HA CAIDO EN EL CASILLERO RUSHERO|||\t")
    elif posicion in casilleros_esp[3]:
        nueva_posicion = hongos_locos(posicion)
        print("\t|||HA CAIDO EN EL CASILLERO HONGOS LOCOS|||\t")
    elif serp_esca(posicion) != 0:
        nueva_posicion = serp_esca(posicion)
    else:
        nueva_posicion = posicion
    modificar_estadisticas(estadisticas, casilleros_esp, posicion)

    print(f"||| SU POSICION AHORA ES > {nueva_posicion}")

    return nueva_posicion


def resetear_estadisticas(estadisticas: list) -> list:
    """
    > Toma las estadisticas y las reinicia
    > Retorna las estadisticas en cero
    """
    estadisticas[0] = 0
    estadisticas[1] = 0
    estadisticas[2] = 0
    estadisticas[3] = 0
    estadisticas[4] = 0
    estadisticas[5] = 0

    return estadisticas


def imprimir_estadistica(partida: int, estadistica: dict) -> None:
    """
    > De acuerdo a si se ha iniciado o no una partida, toma las estadisticas y las imprime.
    > Procedimiento

    """
    if partida == 0:
        print("||| TODAVÍA NO SE HA INICIADO NINGUNA PARTIDA |||")
    else:
        print(f"\t\n||| E S T A D I S T I C A S |||\t\n"
              f"CASCARA DE BANANA > {estadistica[0]}\n"
              f"MAGICO > {estadistica[1]}\n"
              f"RUSHERO > {estadistica[2]}\n"
              f"HONGOS LOCOS > {estadistica[3]}\n"
              f"ESCALERAS > {estadistica[4]}\n"
              f"SERPIENTES > {estadistica[5]}\n")


def procedimiento_juego(jugadores: dict, turno_inicial: int, tablero: list,
                        casilleros_esp: list, estadisticas: list) -> None:
    """
    > Es el procedimiento del juego que se lleva a cabo mientras que no haya ningun ganador.

    """

    ganador: str = ""
    casilleros_especiales: list = casilleros_esp
    turno: int = modificar_turno(jugadores, turno_inicial)

    print(f"\n||| EL JUGADOR A EMPEZAR ES > {jugadores[turno][1]} ||\n")

    while ganador == "":
        print(f"||| LA POSICION ACTUAL DE {jugadores[turno][1]} ES > {jugadores[turno][2]} ")
        ganador = ""
        opcion: int = validar_opcion_modificacion("\n>>PARA TIRAR EL DADO INGRESE (1)<<\n",
                                                  "\n====EL VALOR INGRESADO ES INVÁLIDO====\n",
                                                  1, 1)
        dado: int = tirar_dado(opcion)
        posicion: int = modificar_posicion(jugadores, dado, turno)

        jugadores[turno][2] = casilleros_posicion(posicion, casilleros_especiales, estadisticas)
        posicion_en_tablero(tablero, jugadores, casilleros_especiales)

        if jugadores[turno][2] >= 100:
            ganador = jugadores[turno][1]
            print(f"=============================================="
                  f"|| EL GANADOR DE ESTA PARTIDA ES {ganador} ||"
                  f"==============================================")

        turno = modificar_turno(jugadores, turno)


def main() -> None:

    tablero_sinmodificar: list = crear_tablero()
    turno_inicial: int = 0
    casilleros_especiales: list = random_casilleros()
    contador_cb: int = 0
    contador_ma: int = 0
    contador_ru: int = 0
    contador_hl: int = 0
    contador_es: int = 0
    contador_se: int = 0
    estadisticas = [contador_cb, contador_ma, contador_ru, contador_hl, contador_es, contador_se]
    partida: int = 0
    posicion: int = 0
    opcion: int = 0
    tablero: list = tablero_casillerosesp(casilleros_especiales)

    while opcion != 4:
        menu()
        opcion: int = validar_opcion_modificacion("|||  SELECCIONE UNA OPCION DEL MENU >  \t",
                                                  "\n====EL VALOR INGRESADO ES INVÁLIDO====\n",
                                                  1, 4)
        if opcion == 1:
            bienvenida()
            imprimir_tablero(tablero)
            jugadores: dict = ingresar_jugadores()
            procedimiento_juego(jugadores, turno_inicial, tablero, casilleros_especiales, estadisticas)
            estadisticas: list = modificar_estadisticas(estadisticas, casilleros_especiales, posicion)
            partida += 1
        elif opcion == 2:
            imprimir_estadistica(partida, estadisticas)
        elif opcion == 3:
            resetear_estadisticas(estadisticas)
            imprimir_estadistica(partida, estadisticas)
    despedida()

main()


