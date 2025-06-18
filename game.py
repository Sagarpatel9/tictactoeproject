import random

BOARD_SIZE = 3
MAX_PIECES = 3

class Game:
    def __init__(self):
        self.reset()

    def reset(self, mode="human", starter=None):
        """
        Reset the game state.
        mode: "human" or "ai"
        starter: Optional "X" or "O" (random if None)
        """
        self.board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.move_history = {"X": [], "O": []}
        self.current_player = starter if starter else random.choice(["X", "O"])
        self.phase = 1  # Phase 1: placement, Phase 2: fade-and-replace
        self.winner = None
        self.winning_cells = []
        self.mode = mode  # Save selected mode

    def get_state(self):
        """
        Return the current game state to the frontend.
        """
        return {
            "board": self.board,
            "current_player": self.current_player,
            "phase": self.phase,
            "winner": self.winner,
            "winning_cells": self.winning_cells,
            "mode": self.mode
        }

    def make_move(self, row, col):
        """
        Apply a move for the current player.
        """
        if self.winner or self.board[row][col] != "":
            return False

        player = self.current_player

        # Phase 1: Allow up to MAX_PIECES
        if self.phase == 1 and len(self.move_history[player]) >= MAX_PIECES:
            return False

        # Phase 2: Remove oldest piece
        if self.phase == 2 and len(self.move_history[player]) == MAX_PIECES:
            old_row, old_col = self.move_history[player].pop(0)
            self.board[old_row][old_col] = ""

        self.board[row][col] = player
        self.move_history[player].append((row, col))

        if self.check_win(player):
            self.winner = player

        if self.phase == 1 and len(self.move_history["X"]) == MAX_PIECES and len(self.move_history["O"]) == MAX_PIECES:
            self.phase = 2

        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def check_win(self, symbol):
        """
        Check if the specified symbol has won.
        """
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
