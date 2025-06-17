# app.py

from flask import Flask, render_template, request, jsonify
from game import Game

app = Flask(__name__)
game = Game()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    row, col = data["row"], data["col"]
    game.make_move(row, col)
    return jsonify(game.get_state())

@app.route("/reset", methods=["POST"])
def reset():
    game.reset()
    return jsonify(game.get_state())

if __name__ == "__main__":
    app.run(debug=True)
