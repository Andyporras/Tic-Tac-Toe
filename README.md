# Tic-Tac-Toe con IA - Algoritmo Minimax con Alpha-Beta Pruning

Este proyecto implementa un juego de **Tic-Tac-Toe** (Tres en Línea) con una inteligencia artificial (IA) que utiliza el algoritmo **Minimax** con **Alpha-Beta Pruning** para tomar decisiones inteligentes.
## Algoritmo Minimax con Alpha-Beta Pruning

### ¿Qué es el Algoritmo Minimax?
El algoritmo **Minimax** es un método de toma de decisiones utilizado en juegos de dos jugadores con información completa y sin incertidumbre, como el **Tic-Tac-Toe**. El objetivo de Minimax es maximizar el puntaje para un jugador (en este caso, la IA) mientras minimiza el puntaje del oponente (el jugador humano).

### ¿Cómo Funciona el Algoritmo en Este Proyecto?

El algoritmo evalúa todas las posibles jugadas en el juego y selecciona la mejor jugada posible para la IA. La IA intenta maximizar su puntuación, mientras que el jugador intenta minimizar la puntuación de la IA. A continuación se describen los pasos clave del algoritmo:

1. **Condiciones de Finalización**:
   - Se verifica si hay un ganador utilizando la función `verificar_ganador()`. Si el jugador (X) gana, devuelve `-1`, si la IA (O) gana, devuelve `1`.
   - Si el juego está en empate (es decir, no hay espacio disponible y no hay ganador), se devuelve `0`.
   - Si llega a la profundida maxima(3 o 5 de acuerdo a la dificulta) se devuelve `0`.

2. **Recursión para el Maximizador (IA)**:
   - Si es el turno de la IA (maximizador), intenta maximizar su puntaje.
   - Evalúa todas las jugadas posibles, realizando cada jugada en el tablero y luego recursivamente evaluando la siguiente jugada hasta llegar a una condición de finalización(Profundida 3 para Intermedio y 5 para Avanzado).
   - Utiliza **Alpha-Beta Pruning** para reducir el número de ramas que deben evaluarse, evitando calcular jugadas innecesarias que no afectarán el resultado final.

3. **Recursión para el Minimizador (Jugador)**:
   - Si es el turno del jugador (minimizador), intenta minimizar el puntaje de la IA.
   - Similar al maximizador, evalúa las jugadas posibles y utiliza la Alpha-Beta Pruning para optimizar la búsqueda.

4. **Alpha-Beta Pruning**:
   - La **Alpha-Beta Pruning** es una optimización del algoritmo Minimax que permite reducir el número de nodos a explorar. La poda se produce cuando el algoritmo determina que una rama no afectará el resultado final, ahorrando tiempo de cálculo.

### Flujo del Algoritmo

1. Comienza con la verificación de si el juego ha terminado o si se necesita más evaluación.
2. Si es el turno de la IA, intenta maximizar el puntaje, recorriendo todas las posibles jugadas.
3. Si es el turno del jugador, intenta minimizar el puntaje de la IA, recorriendo todas las posibles jugadas.
4. Continúa recursivamente evaluando hasta encontrar una jugada óptima.
5. Devuelve la mejor jugada para el jugador de turno.

### Funciones Principales
- **minimax(profundidad, es_maximizador, alpha, beta)**: Función recursiva que evalúa todas las jugadas posibles y devuelve el mejor puntaje.
- **verificar_ganador()**: Verifica si hay un ganador en el tablero.
- **hay_empate()**: Verifica si el juego ha terminado en empate.
- **mejor_movimiento(profundidad)**: Encuentra la mejor jugada para la IA utilizando el algoritmo Minimax.

### Conclusiones
Este algoritmo permite que la IA juegue de manera inteligente contra un jugador humano. La combinación de Minimax con Alpha-Beta Pruning optimiza la toma de decisiones, reduciendo significativamente el número de jugadas que la IA debe evaluar. Esto hace que la IA sea capaz de competir de manera eficiente en juegos de Tic-Tac-Toe con diferentes niveles de dificultad.


### Notas
En los modos **Intermedio** y **Avanzado**, el juego generalmente termina en empate o con la IA ganando, lo que demuestra que la inteligencia artificial es bastante efectiva. En cambio, en el modo **Principiante**, los movimientos aleatorios de la IA hacen que sea fácil ganar.
