# konstruktor, przyjmujący jako pierwszy parametr, pole na którym znajduje się figura
# metodę publiczną list_available_moves(), wypisującą dozwolone ruchy
# metodę publiczną validate_move(dest_field), informującą, czy możliwy jest ruch na wskazane pole.
letter_fields = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
number_fields = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}


def decode_field(field):
    list_f = list(field)
    return tuple([letter_fields.get(list_f[0]), number_fields.get(int(list_f[1]))])


def code_field(tuple_field):
    key_list_letters = list(letter_fields.keys())
    val_list_letters = list(letter_fields.values())
    key_list_numbers = list(number_fields.keys())
    val_list_numbers = list(number_fields.values())

    field_letter = str(key_list_letters[val_list_letters.index(tuple_field[0])])
    field_number = str(key_list_numbers[val_list_numbers.index(tuple_field[1])])

    return str(field_letter + field_number)


class Figure:
    available_moves = []
    # current_field = 'a8'

    def __init__(self, field):
        self.field = field

    @property
    def list_available_moves(self):
        lst = []
        coded_lst = []
        current_field = decode_field(self.field)

        for move in self.available_moves:
            single_move = tuple(a + b for a, b in zip(move, current_field))
            # verify if still on the chessboard
            if single_move[0] <= 8 and single_move[1] <= 8:
                lst.append(single_move)

        for el in lst:
            coded_lst.append(code_field(el))

        return coded_lst

    def validate_move(self, dest_field):
        pass


# The king may move to any adjoining square. No move may be made such that the king is placed or left in check.
# The king may participate in castling, which is a move consisting of the king moving two squares toward
# a same-colored rook on the same rank and the rook moving to the square crossed by the king.
# Castling may only be performed if the king and rook involved are unmoved, if the king is not in check,
# if the king would not travel through or into check, and if there are no pieces between the rook and the king.
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


# The queen may move any number of squares vertically, horizontally, or diagonally without jumping.
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


# The rook may move any number of squares vertically or horizontally without jumping.
# It also takes part, along with the king, in castling.
class Rook(Figure):
    available_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up  # down  # left  # right


# The bishop may move any number of squares diagonally without jumping.
# Consequently, a bishop stays on squares of the same color throughout the game.
class Bishop(Figure):
    available_moves = [
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]


# The knight moves from one corner of any two-by-three rectangle to the opposite corner.
# Consequently, the knight alternates its square color each time it moves. It is not obstructed by other pieces.
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


# The pawn may move forward one square, and one or two squares when on its starting square,
# toward the opponent's side of the board. When there is an enemy piece one square diagonally ahead of a pawn, '
# ('then the pawn may capture that piece. A pawn can perform a special type of capture of an enemy pawn called '
# 'en passant ("in passing"), wherein it captures a horizontally adjacent enemy pawn that has just advanced two squares as if that pawn had only advanced one square. If the pawn reaches a square on the back rank of the opponent, '))
# 'it promotes to the player')s choice of a queen, rook, bishop, or knight of the same color.[6]
class Pawn(Figure):
    pass
