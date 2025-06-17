# game.py

BOARD_SIZE = 3
MAX_PIECES = 3

class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.move_history = {"X": [], "O": []}
        self.current_player = "X"
        self.phase = 1
        self.winner = None
        self.winning_cells = []  # ✅ Add this


    def get_state(self):
        return {
            "board": self.board,
            "current_player": self.current_player,
            "phase": self.phase,
            "winner": self.winner
        }

    def make_move(self, row, col):
        if self.winner or self.board[row][col] != "":
            return False

        player = self.current_player

        if self.phase == 1 and len(self.move_history[player]) >= MAX_PIECES:
            return False

        if self.phase == 2 and len(self.move_history[player]) == MAX_PIECES:
            old_row, old_col = self.move_history[player].pop(0)
            self.board[old_row][old_col] = ""

        self.board[row][col] = player
        self.move_history[player].append((row, col))

        if self.check_win(player):
            self.winner = player

        if self.phase == 1 and len(self.move_history["X"]) == 3 and len(self.move_history["O"]) == 3:
            self.phase = 2

        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def check_win(self, symbol):
        for i in range(BOARD_SIZE):
            if all(self.board[i][j] == symbol for j in range(BOARD_SIZE)):
                self.winning_cells = [(i, j) for j in range(BOARD_SIZE)]
                return True
            if all(self.board[j][i] == symbol for j in range(BOARD_SIZE)):
                self.winning_cells = [(j, i) for j in range(BOARD_SIZE)]
                return True
        if all(self.board[i][i] == symbol for i in range(BOARD_SIZE)):
            self.winning_cells = [(i, i) for i in range(BOARD_SIZE)]
            return True
        if all(self.board[i][BOARD_SIZE - i - 1] == symbol for i in range(BOARD_SIZE)):
            self.winning_cells = [(i, BOARD_SIZE - i - 1) for i in range(BOARD_SIZE)]
            return True
        return False

    def get_state(self):
        return {
            "board": self.board,
            "current_player": self.current_player,
            "phase": self.phase,
            "winner": self.winner,
            "winning_cells": self.winning_cells if hasattr(self, 'winning_cells') else []
        }
