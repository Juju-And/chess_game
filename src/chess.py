letter_fields = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
number_fields = {
    1: 7,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1,
    8: 0,
}  # "field": array_position


def decode_field(field):
    list_f = [field[0:1], field[1 : len(field)]]
    pos_x = letter_fields.get(list_f[0])
    pos_y = number_fields.get(int(list_f[1]))

    if not None in (pos_x, pos_y):
        return tuple([pos_x, pos_y])
    else:
        return None


def code_field(tuple_field):
    if verify_position_on_chessboard(tuple_field) is not None:
        key_list_letters = list(letter_fields.keys())
        val_list_letters = list(letter_fields.values())
        key_list_numbers = list(number_fields.keys())
        val_list_numbers = list(number_fields.values())

        field_letter = str(key_list_letters[val_list_letters.index(tuple_field[0])])
        field_number = str(key_list_numbers[val_list_numbers.index(tuple_field[1])])

        return str(field_letter + field_number)


def verify_position_on_chessboard(field):
    # print(field[0])
    if not (
        int(field[0]) <= 7
        and int(field[1]) <= 7
        and int(field[0]) >= 0
        and int(field[1]) >= 0
    ):
        return None
    else:
        return field


class Figure:
    available_moves = []

    def __init__(self, field):
        self.field = field

    @property
    def list_available_moves(self):
        lst = []
        coded_lst = []
        current_field = decode_field(self.field)

        if current_field is None:
            return []

        for move in self.available_moves:
            if current_field is None:
                return []
            else:
                single_move = tuple(a + b for a, b in zip(move, current_field))
                if verify_position_on_chessboard(single_move) is not None:
                    lst.append(single_move)
        for el in lst:
            coded_lst.append(code_field(el))

        return coded_lst

    def validate_move(self, dest_field):
        moves = self.list_available_moves
        if dest_field in moves:
            return "valid"
        else:
            return "not valid"


class King(Figure):
    available_moves = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]


class Queen(Figure):  # królowa, hetman
    available_moves = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]


class Rook(Figure):
    available_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up  # down  # left  # right


class Bishop(Figure):
    available_moves = [
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]


class Knight(Figure):
    available_moves = [
        (-2, -1),
        (-2, 1),  # two up, one left/right
        (2, -1),
        (2, 1),  # two down, one left/right
        (-1, -2),
        (-1, 2),  # one up, two left/right
        (1, -2),
        (1, 2),  # one down, two left/right
    ]


class Pawn(Figure):
    available_moves = [(-1, 0), (1, 0)]


CHESS_PIECES = {
    "king": King,
    "queen": Queen,
    "bishop": Bishop,
    "knight": Knight,
    "rook": Rook,
    "pawn": Pawn,
}


def validate_figure(figure):
    return CHESS_PIECES.get(figure)
