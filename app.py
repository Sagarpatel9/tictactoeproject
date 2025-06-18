from flask import Flask, render_template, request, jsonify
from game import Game
from ai_agent import get_best_move  #  AI logic to pick best move

app = Flask(__name__)
game = Game()  # Initialize a new game

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    row, col = data["row"], data["col"]
    game.make_move(row, col)

    # If AI's turn after human move
    if not game.winner and game.mode == "ai" and game.current_player == "O":
        ai_row, ai_col = get_best_move(game.board, game.move_history, game.current_player, game.phase)
        game.make_move(ai_row, ai_col)

    return jsonify(game.get_state())

@app.route("/reset", methods=["POST"])
def reset():
    data = request.get_json()
    mode = data.get("mode", "human")
    starter = data.get("starter", "X")  # default starter is human (X)

    game.reset(mode=mode, starter=starter)

    # If AI is starter and it's AI mode, make AI's first move
    if game.mode == "ai" and game.current_player == "O":
        ai_row, ai_col = get_best_move(game.board, game.move_history, game.current_player, game.phase)
        game.make_move(ai_row, ai_col)

    return jsonify(game.get_state())

if __name__ == "__main__":
    app.run(debug=True)
