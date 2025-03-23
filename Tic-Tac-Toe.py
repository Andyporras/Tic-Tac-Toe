import pygame
import math
import random

# Inicialización de Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 300, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GRAY = (150, 150, 150)

# Fuente
FONT = pygame.font.Font(None, 36)

# Matriz del juego
tablero = [[" " for _ in range(3)] for _ in range(3)]
modo = 1  # Modo por defecto: Principiante

# Función para dibujar el tablero
def dibujar_tablero():
    SCREEN.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(SCREEN, BLACK, (0, i * 100), (300, i * 100), 3)
        pygame.draw.line(SCREEN, BLACK, (i * 100, 0), (i * 100, 300), 3)
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "X":
                color = RED
            elif tablero[i][j] == "O":
                color = BLUE
            else:
                continue
            text = FONT.render(tablero[i][j], True, color)
            SCREEN.blit(text, (j * 100 + 40, i * 100 + 30))
    pygame.display.flip()

def verificar_ganador():
    # Verificar fila
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
            return tablero[i][0]
    # Verificar columna
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return tablero[0][i]
    # Verificar diagonal
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]
    # Verificar diagonal
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]
    return " "

def hay_empate():
    for fila in tablero:
        for celda in fila:
            if celda == " ":
                return False
    return True

def obtener_menor(a , b):
    if a < b:
        return a
    return b
def obtener_mayor(a, b):
    if a > b:
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
        mejor_puntaje = -math.inf
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = "O"
                    puntaje = minimax(profundidad + 1, False, alpha, beta)
                    tablero[i][j] = " "
                    mejor_puntaje = obtener_mayor(puntaje, mejor_puntaje)
                    alpha = obtener_mayor(alpha, puntaje)
                    if beta <= alpha:
                        break
        return mejor_puntaje
    else:
        mejor_puntaje = math.inf
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
    mejor_puntaje = -math.inf
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

def seleccionar_modo():
    global modo
    SCREEN.fill(WHITE)
    textos = ["1. Principiante", "2. Intermedio", "3. Avanzado", "4. Salir"]
    for i, texto in enumerate(textos):
        rect = pygame.Rect(50, 50 + i * 60, 200, 50)
        pygame.draw.rect(SCREEN, GRAY, rect)
        text = FONT.render(texto, True, BLACK)
        SCREEN.blit(text, (60, 60 + i * 60))
    pygame.display.flip()
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando = False
                modo = 4
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 <= x <= 250:
                    if 50 <= y <= 100:
                        modo = 1
                        esperando = False
                    elif 110 <= y <= 160:
                        modo = 2
                        esperando = False
                    elif 170 <= y <= 220:
                        modo = 3
                        esperando = False
                    #Si selecciona salir se cierra el juego
                    elif 230 <= y <= 280:
                        esperando = False
                        pygame.quit()
                        exit()

def jugar():
    global modo
    seleccionar_modo()
    profundidad = 0
    if modo == 2:
        profundidad = 3
    elif modo == 3:
        profundidad = 5
    jugador = "X"
    corriendo = True
    while corriendo:
        dibujar_tablero()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN and jugador == "X":
                x, y = event.pos
                fila, col = y // 100, x // 100
                if tablero[fila][col] == " ":
                    tablero[fila][col] = "X"
                    jugador = "O"
        if jugador == "O" and corriendo:
            if modo == 1:
                while True:
                    x, y = random.randint(0, 2), random.randint(0, 2)
                    if tablero[x][y] == " ":
                        tablero[x][y] = "O"
                        break
            else:
                mov = mejor_movimiento(profundidad)
                tablero[mov[0]][mov[1]] = "O"
            jugador = "X"
        ganador = verificar_ganador()
        if ganador != " " or hay_empate():
            dibujar_tablero()
            pygame.time.delay(2000)
            corriendo = False
    # Mensaje de fin de juego y reinicio 
    if ganador == " ":
        mensaje = "Empate!"
    else:
        mensaje = f"Ganador: {ganador}"
    SCREEN.fill(WHITE)
    text = FONT.render(mensaje, True, BLACK)
    SCREEN.blit(text, (50, 150))
    pygame.display.flip()
    pygame.time.delay(2000)
    # Reinicio del juego
    for i in range(3):
        for j in range(3):
            tablero[i][j] = " "
    jugar
jugar()
