from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        data = {
            "Modules": 15,
            "Subject": "Data Structures and Algorithms",
        }
        return jsonify(data)

@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def display_possible_moves(chess_figure,current_field):
    figure = None

    data = {
       "availableMoves":[
          "H3"
       ],
       "error": None,
       "figure": chess_figure,
       "currentField": current_field
    }
    return jsonify(data)

@app.route('/api/v1/<chess_figure>/<current_field>/<dest_field>', methods=['GET'])
def display_possible_moves(chess_figure,current_field,dest_field):
    figure = None

    data = {
            "move": "valid",
            "figure": chess_figure,
            "error": None,
            "currentField": current_field,
            "destField": dest_field
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()