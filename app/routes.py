from flask import Flask, request, jsonify
from chess import King, Queen, Bishop

king = King("a8")
queen = Queen("a8")
bishop = Bishop("a8")

CHESS = {"king": king, "queen": queen, "bishop": bishop}


app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def display_possible_moves(chess_figure, current_field):
    figure = CHESS.get(chess_figure)
    figure.field = current_field

    data = {
        "availableMoves": figure.list_available_moves,
        "error": None,
        "figure": chess_figure,
        "currentField": current_field,
    }

    return jsonify(data)


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validate_possible_moves(chess_figure, current_field, dest_field):
    figure = None

    data = {
        "move": "valid",
        "figure": chess_figure,
        "error": None,
        "currentField": current_field,
        "destField": dest_field,
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
