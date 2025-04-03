# Tic-Tac-Toe with AI - Minimax Algorithm with Alpha-Beta Pruning

This project implements a **Tic-Tac-Toe** game with artificial intelligence (AI) using the **Minimax** algorithm with **Alpha-Beta Pruning** to make intelligent decisions.

## Minimax Algorithm with Alpha-Beta Pruning

### What is the Minimax Algorithm?

The **Minimax** algorithm is a decision-making method used in two-player games with complete information and no uncertainty, such as **Tic-Tac-Toe**. The goal of Minimax is to maximize the score for one player (in this case, the AI) while minimizing the score for the opponent (the human player).

### How Does the Algorithm Work in This Project?

The algorithm evaluates all possible moves in the game and selects the best possible move for the AI. The AI tries to maximize its score, while the player tries to minimize the AI's score. Here are the key steps of the algorithm:

1. **Termination Conditions**:
   - It checks if there's a winner using the `check_winner()` function. If the player (X) wins, it returns `-1`; if the AI (O) wins, it returns `1`.
   - If the game is a draw (i.e., no available spaces left and no winner), it returns `0`.
   - If it reaches the maximum depth (3 or 5 depending on difficulty), it returns `0`.

2. **Recursion for the Maximizing Player (AI)**:
   - If it's the AI's turn (maximizer), it tries to maximize its score.
   - It evaluates all possible moves, makes each move on the board, and recursively evaluates the next move until reaching a termination condition (depth 3 for Intermediate and 5 for Advanced).
   - It uses **Alpha-Beta Pruning** to reduce the number of branches that need evaluation, avoiding unnecessary calculations that won't affect the final outcome.

3. **Recursion for the Minimizing Player (Human)**:
   - If it's the player's turn (minimizer), it tries to minimize the AI's score.
   - Similar to the maximizer, it evaluates possible moves and uses Alpha-Beta Pruning to optimize the search.

4. **Alpha-Beta Pruning**:
   - **Alpha-Beta Pruning** is an optimization of the Minimax algorithm that reduces the number of nodes to explore. Pruning occurs when the algorithm determines that a branch won't affect the final outcome, saving computation time.

### Algorithm Flow

1. Starts with checking if the game has ended or needs further evaluation.
2. If it's the AI's turn, it tries to maximize the score by exploring all possible moves.
3. If it's the player's turn, it tries to minimize the AI's score by exploring all possible moves.
4. Continues recursively evaluating until finding an optimal move.
5. Returns the best move for the current player's turn.

### Key Functions
- **minimax(depth, is_maximizing_player, alpha, beta)**: Recursive function that evaluates all possible moves and returns the best score.
- **check_winner()**: Checks if there's a winner on the board.
- **is_draw()**: Checks if the game has ended in a draw.
- **best_move(depth)**: Finds the best move for the AI using the Minimax algorithm.

### Conclusions
This algorithm allows the AI to play intelligently against a human player. The combination of Minimax with Alpha-Beta Pruning optimizes decision-making, significantly reducing the number of moves the AI needs to evaluate. This enables the AI to compete efficiently in Tic-Tac-Toe games with different difficulty levels.

### Notes
In **Intermediate** and **Advanced** modes, the game usually ends in a draw or with the AI winning, demonstrating the effectiveness of the artificial intelligence. In contrast, in **Beginner** mode, the AI's random moves make it easy to win.
