# ai_agent.py 
import copy

BOARD_SIZE = 3  # Standard Tic Tac Toe board size (3x3)


def get_best_move(board, move_history, player, phase):
    """
    Determines the best move for the current player using the minimax algorithm.
    Supports both placement and fading phases (Phase 1 and 2).
    """
    opponent = "X" if player == "O" else "O"
    best_score = float("-inf")
    best_move = None

    # Loop through all cells to evaluate possible moves
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] != "":
                continue  # Skip already filled cells

            # Simulate a move on a deep copy of the board and move history
            new_board = copy.deepcopy(board)
            new_history = {k: v[:] for k, v in move_history.items()}

            # If phase 2 and player has 3 tokens, remove the oldest before placing a new one
            if phase == 2 and len(new_history[player]) == 3:
                old_r, old_c = new_history[player].pop(0)
                new_board[old_r][old_c] = ""

            # Place the new move
            new_board[r][c] = player
            new_history[player].append((r, c))

            # Evaluate the move using minimax
            score = minimax(new_board, new_history, phase, False, player, opponent, 0, 6)

            # Update best move if this one is better
            if score > best_score:
                best_score = score
                best_move = (r, c)

    return best_move


def minimax(board, move_history, phase, is_maximizing, ai_player, human_player, depth, max_depth):
    """
    Recursive minimax algorithm to evaluate board states.
    Returns a score based on winning, losing, or drawing from the AI's perspective.
    """
    # Terminal conditions
    if check_win(board, ai_player):
        return 10 - depth  # AI wins
    if check_win(board, human_player):
        return depth - 10  # Human wins
    if all(cell != "" for row in board for cell in row) or depth >= max_depth:
        return 0  # Draw or max depth reached

    current_player = ai_player if is_maximizing else human_player
    best_score = float("-inf") if is_maximizing else float("inf")

    # Try all possible moves
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] != "":
                continue

            new_board = copy.deepcopy(board)
            new_history = {k: v[:] for k, v in move_history.items()}

            # Handle fading logic in phase 2
            if phase == 2 and len(new_history[current_player]) == 3:
                old_r, old_c = new_history[current_player].pop(0)
                new_board[old_r][old_c] = ""

            new_board[r][c] = current_player
            new_history[current_player].append((r, c))

            # Recursive call for next move
            score = minimax(new_board, new_history, phase, not is_maximizing,
                            ai_player, human_player, depth + 1, max_depth)

            # Update best score based on whether we're maximizing or minimizing
            if is_maximizing:
                best_score = max(best_score, score)
            else:
                best_score = min(best_score, score)

    return best_score


def check_win(board, symbol):
    """
    Checks if the given symbol ('X' or 'O') has won the game.
    """
    for i in range(BOARD_SIZE):
        # Check rows and columns
        if all(board[i][j] == symbol for j in range(BOARD_SIZE)):
            return True
        if all(board[j][i] == symbol for j in range(BOARD_SIZE)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - i - 1] == symbol for i in range(BOARD_SIZE)):
        return True
    return False
