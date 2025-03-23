import math
import random

# Matriz del juego
tablero = [[" " for _ in range(3)] for _ in range(3)] 

def seleccionar_modo():
    print("Seleccione el nivel de dificultad:")
    print("1. Principiante")
    print("2. Intermedio")
    print("3. Avanzado")
    modo = int(input())
    return modo

def imprimir_tablero():
    for fila in tablero:
        print(fila)

def verificar_ganador():
    # Comprobar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
            return tablero[i][0]
    # Comprobar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
    # Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    return " "

def hay_empate():
    for fila in tablero:
        for celda in fila:
            if celda == " ":
                return False
    return True

def obtener_menor(a, b):
    """Función que devuelve el menor de dos valores."""
    if a < b:
        return a
    return b

def minimax(profundidad, es_maximizador, alpha, beta):
    ganador = verificar_ganador()
    if ganador == "X":
        return -1
    if ganador == "O":
        return 1
    if hay_empate():
        return 0
    if es_maximizador:
        mejor_puntaje = -math.inf # -infinito
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = "O"
                    puntaje = minimax(profundidad + 1, False, alpha, beta)
                    tablero[i][j] = " "
                    mejor_puntaje = max(puntaje, mejor_puntaje)
                    alpha = max(alpha, puntaje) 
                    if beta <= alpha:
                        break
        return mejor_puntaje
    else:
        mejor_puntaje = math.inf # infinito
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = "X"
                    puntaje = minimax(profundidad + 1, True, alpha, beta)
                    tablero[i][j] = " "
                    mejor_puntaje = obtener_menor(puntaje, mejor_puntaje)
                    beta = obtener_menor(beta, puntaje)
                    if beta <= alpha:
                        break
        return mejor_puntaje

def mejor_movimiento(profundidad):
    mejor_puntaje = -math.inf # -infinito
    mejor_mov = (-1, -1)
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = "O"
                puntaje = minimax(profundidad, False, -math.inf, math.inf)
                tablero[i][j] = " "
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_mov = (i, j)
    return mejor_mov

def jugar():
    print("Bienvenido a Tic-Tac-Toc")
    print("Jugador: X")
    print("IA: O")
    print("Seleccione la posición de la matriz (0-2)")

    modo = seleccionar_modo()
    profundidad = 0
    if modo == 2:
        profundidad = 3
    elif modo == 3:
        profundidad = 5

    while True:
        imprimir_tablero()
        print("Turno del jugador X")
        x = int(input("Ingrese la fila (0-2): "))
        y = int(input("Ingrese la columna (0-2): "))
        if tablero[x][y] == " ":
            tablero[x][y] = "X"
        else:
            print("Posición ocupada, intente de nuevo")
            continue

        if verificar_ganador() == "X":
            imprimir_tablero()
            print("¡Felicidades! Has ganado")
            break
        if hay_empate():
            imprimir_tablero()
            print("¡Empate!")
            break

        print("Turno de la IA (O)")
        if modo == 1:
            while True:
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if tablero[x][y] == " ":
                    tablero[x][y] = "O"
                    break
        else:
            mov = mejor_movimiento(profundidad)
            tablero[mov[0]][mov[1]] = "O"

        if verificar_ganador() == "O":
            imprimir_tablero()
            print("¡La IA ha ganado!")
            break
        if hay_empate():
            imprimir_tablero()
            print("¡Empate!")
            break

jugar()
