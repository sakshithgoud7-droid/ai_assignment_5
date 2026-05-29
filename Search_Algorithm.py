import math
import random
from copy import deepcopy


# Tic Tac Toe Game

class TicTacToe:

    def __init__(self):
        self.board = [" "] * 9

    def show_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()

    def get_moves(self):
        moves = []

        for i in range(9):
            if self.board[i] == " ":
                moves.append(i)

        return moves

    def play(self, pos, symbol):
        if self.board[pos] == " ":
            self.board[pos] = symbol
            return True

        return False

    def remove(self, pos):
        self.board[pos] = " "

    def check_winner(self):

        patterns = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for p in patterns:
            a, b, c = p

            if self.board[a] == self.board[b] == self.board[c] \
                    and self.board[a] != " ":
                return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None


# Minimax Algorithm

def minimax(game, depth, is_max):

    result = game.check_winner()

    if result == "X":
        return 1

    if result == "O":
        return -1

    if result == "Draw":
        return 0

    if is_max:

        best_score = -math.inf

        for move in game.get_moves():

            game.play(move, "X")

            score = minimax(game, depth + 1, False)

            game.remove(move)

            if score > best_score:
                best_score = score

        return best_score

    else:

        best_score = math.inf

        for move in game.get_moves():

            game.play(move, "O")

            score = minimax(game, depth + 1, True)

            game.remove(move)

            if score < best_score:
                best_score = score

        return best_score


# Alpha Beta Pruning

def alpha_beta(game, depth, alpha, beta, is_max):

    result = game.check_winner()

    if result == "X":
        return 1

    if result == "O":
        return -1

    if result == "Draw":
        return 0

    if is_max:

        value = -math.inf

        for move in game.get_moves():

            game.play(move, "X")

            score = alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                False
            )

            game.remove(move)

            value = max(value, score)

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in game.get_moves():

            game.play(move, "O")

            score = alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                True
            )

            game.remove(move)

            value = min(value, score)

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


# Simple Evaluation Function

def evaluate(game):

    score = 0

    patterns = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for p in patterns:

        values = [game.board[i] for i in p]

        if values.count("X") == 2 and values.count(" ") == 1:
            score += 5

        if values.count("O") == 2 and values.count(" ") == 1:
            score -= 5

    return score


# Heuristic Alpha Beta

def heuristic_search(game, depth, alpha, beta, is_max):

    result = game.check_winner()

    if result == "X":
        return 100

    if result == "O":
        return -100

    if result == "Draw":
        return 0

    if depth == 0:
        return evaluate(game)

    if is_max:

        best = -math.inf

        for move in game.get_moves():

            game.play(move, "X")

            value = heuristic_search(
                game,
                depth - 1,
                alpha,
                beta,
                False
            )

            game.remove(move)

            best = max(best, value)

            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:

        best = math.inf

        for move in game.get_moves():

            game.play(move, "O")

            value = heuristic_search(
                game,
                depth - 1,
                alpha,
                beta,
                True
            )

            game.remove(move)

            best = min(best, value)

            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


# Monte Carlo Simulation

def random_game(game, turn):

    current = turn

    while True:

        result = game.check_winner()

        if result is not None:
            return result

        move = random.choice(game.get_moves())

        game.play(move, current)

        if current == "X":
            current = "O"
        else:
            current = "X"


def mcts(game, runs=500):

    best_move = None
    best_wins = -1

    for move in game.get_moves():

        total_wins = 0

        for _ in range(runs):

            temp = deepcopy(game)

            temp.play(move, "X")

            result = random_game(temp, "O")

            if result == "X":
                total_wins += 1

        if total_wins > best_wins:
            best_wins = total_wins
            best_move = move

    return best_move


# Driver Code

game = TicTacToe()

game.play(0, "X")
game.play(4, "O")
game.play(1, "X")

print("Current Board:")
game.show_board()

print("Minimax:", minimax(game, 0, True))

print(
    "Alpha Beta:",
    alpha_beta(game, 0, -math.inf, math.inf, True)
)

print(
    "Heuristic Search:",
    heuristic_search(game, 3, -math.inf, math.inf, True)
)

print(
    "MCTS Best Move:",
    mcts(game, 100)
)
