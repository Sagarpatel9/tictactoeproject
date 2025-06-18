# ai_agent.py

import copy

BOARD_SIZE = 3


def get_best_move(board, move_history, player, phase):
    opponent = "X" if player == "O" else "O"
    best_score = float("-inf")
    best_move = None

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] != "":
                continue

            new_board = copy.deepcopy(board)
            new_history = {k: v[:] for k, v in move_history.items()}

            if phase == 2 and len(new_history[player]) == 3:
                old_r, old_c = new_history[player].pop(0)
                new_board[old_r][old_c] = ""

            new_board[r][c] = player
            new_history[player].append((r, c))

            score = minimax(new_board, new_history, phase, False, player, opponent, 0, 6)

            if score > best_score:
                best_score = score
                best_move = (r, c)

    return best_move


def minimax(board, move_history, phase, is_maximizing, ai_player, human_player, depth, max_depth):
    winner = check_win(board, ai_player)
    if winner:
        return 10 - depth
    if check_win(board, human_player):
        return depth - 10

    if all(cell != "" for row in board for cell in row) or depth >= max_depth:
        return 0

    current_player = ai_player if is_maximizing else human_player
    best_score = float("-inf") if is_maximizing else float("inf")

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            if board[r][c] != "":
                continue

            new_board = copy.deepcopy(board)
            new_history = {k: v[:] for k, v in move_history.items()}

            if phase == 2 and len(new_history[current_player]) == 3:
                old_r, old_c = new_history[current_player].pop(0)
                new_board[old_r][old_c] = ""

            new_board[r][c] = current_player
            new_history[current_player].append((r, c))

            score = minimax(new_board, new_history, phase, not is_maximizing,
                            ai_player, human_player, depth + 1, max_depth)

            if is_maximizing:
                best_score = max(best_score, score)
            else:
                best_score = min(best_score, score)

    return best_score


def check_win(board, symbol):
    for i in range(BOARD_SIZE):
        if all(board[i][j] == symbol for j in range(BOARD_SIZE)):
            return True
        if all(board[j][i] == symbol for j in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == symbol for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - i - 1] == symbol for i in range(BOARD_SIZE)):
        return True
    return False
