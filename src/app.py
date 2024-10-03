import json

from flask import Flask, Response
from src.chess import CHESS_PIECES, validate_figure, decode_field

app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def display_possible_moves(chess_figure, current_field):
    if validate_figure(chess_figure) is None:
        data = {
            "availableMoves": '[]',
            "error": "Invalid figure.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return Response(json.dumps(data), status=404, mimetype='application/json')

    if decode_field(current_field) is None:
        data = {
            "availableMoves": '[]',
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return Response(json.dumps(data), status=409, mimetype='application/json')

    figure = CHESS_PIECES.get(chess_figure)(current_field)
    data = {
        "availableMoves": figure.list_available_moves,
        "error": None,
        "figure": chess_figure,
        "currentField": current_field,
    }
    return Response(json.dumps(data), status=200, mimetype='application/json')


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validate_possible_moves(chess_figure, current_field, dest_field):
    if validate_figure(chess_figure) is None:
        data = {
            "availableMoves": '[]',
            "error": "Invalid figure.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return Response(json.dumps(data), status=404, mimetype='application/json')

    if decode_field(current_field) is None:
        data = {
            "availableMoves": '[]',
            "error": "Field does not exist.",
            "figure": chess_figure,
            "currentField": current_field,
        }
        return Response(json.dumps(data), status=409, mimetype='application/json')

    figure = CHESS_PIECES.get(chess_figure)(current_field)

    if figure.validate_move(dest_field) == 'not valid':
        data = {
            "move": 'invalid',
            "figure": chess_figure,
            "error": "Current move is not permitted.",
            "currentField": current_field,
            "destField": dest_field,
        }
        return Response(json.dumps(data), status=409, mimetype='application/json')
    else:
        data = {
            "move": 'valid',
            "figure": chess_figure,
            "error": None,
            "currentField": current_field,
            "destField": dest_field,
        }
        return Response(json.dumps(data), status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run()
