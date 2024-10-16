from typing import Tuple

from flask import Flask, Response, jsonify
from src.chess import CHESS_PIECES, validate_figure, decode_field

app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def display_possible_moves(chess_figure: str, current_field: str) -> Tuple[Response, int]:
    if validate_figure(chess_figure) is None:
        data = {
            "availableMoves": "[]",
            "error": "Invalid figure.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return jsonify(data), 404

    if decode_field(current_field) is None:
        data = {
            "availableMoves": "[]",
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return jsonify(data), 409

    figure = CHESS_PIECES.get(chess_figure)(current_field)
    data = {
        "availableMoves": figure.list_available_moves,
        "error": None,
        "figure": chess_figure,
        "currentField": current_field,
    }
    return jsonify(data), 200


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validate_possible_moves(chess_figure: str, current_field: str, dest_field: str) -> Tuple[Response, int]:
    if validate_figure(chess_figure) is None:
        data = {
            "availableMoves": [],
            "error": "Invalid figure.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return jsonify(data), 404

    if decode_field(current_field) is None:
        data = {
            "availableMoves": "[]",
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return jsonify(data), 409

    figure = CHESS_PIECES.get(chess_figure)(current_field)

    if not figure.validate_move(dest_field):
        data = {
            "move": "invalid",
            "figure": chess_figure,
            "error": "Current move is not permitted.",
            "currentField": current_field,
            "destField": dest_field,
        }
        return jsonify(data), 409
    else:
        data = {
            "move": "valid",
            "figure": chess_figure,
            "error": None,
            "currentField": current_field,
            "destField": dest_field,
        }
        return jsonify(data), 200


if __name__ == "__main__":
    app.run()
