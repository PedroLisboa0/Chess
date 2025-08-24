def check_capture(new_square, pieces, white_pieces, black_pieces):
    for piece in pieces:
        if piece.pos == new_square.pos:
            pieces.remove(piece)
            new_square.piece_on = None
            match piece.color:
                case "white": white_pieces.remove(piece)
                case "black": black_pieces.remove(piece)


def change_turn(current_turn):
    if current_turn == "white":
        current_turn = "black"
    else:
        current_turn = "white"
    return current_turn


def get_bishop_moves(possible_square, current_square):
    legal_bishop_moves = []
    if possible_square.default_color == current_square.default_color:
        legal_bishop_moves.append(possible_square)
    return legal_bishop_moves


def get_rook_moves(possible_square, current_square):
    legal_rook_moves = []
    if possible_square.x == current_square.x or possible_square.y == current_square.y:
        legal_rook_moves.append(possible_square)
    return legal_rook_moves


def to_notation(position):
    alphabet = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h"
    }
    notation = alphabet[position[0]] + str(9 - (position[1] + 1))
    return notation


def get_enemy_color(color):
    if color == "white":
        enemy_color = "black"
    else:
        enemy_color = "white"
    return enemy_color


class Game:
    def __init__(self):
        self.possible_moves = []
        self.move_counter = 0

    def get_moves(self, piece, squares):
        square_index = 0
        self.possible_moves = []
        directions = piece.directions

        # Finds the index of the square in the flat list, so it can calculate legal moves.
        for square in squares:
            if piece.pos == square.pos:
                square_index = squares.index(square)
                break

        current_square = squares[square_index]
        directional_counter = 0

        if piece.type == "pawn":
            # Changes pawn movement based on context
            if piece.already_moved:
                piece.range = 1

        for direction in directions:
            enemy_piece_blocking = False
            directional_counter += 1
            for i in range(piece.range):
                if enemy_piece_blocking is True:
                    break

                possible_square_index = square_index + direction * (i + 1)
                possible_square = squares[possible_square_index]

                if possible_square.piece_on is not None:
                    if possible_square.piece_on.color == piece.color:
                        break
                    elif possible_square.piece_on.color != piece.color and piece.range != 1:
                        enemy_piece_blocking = True

                if 0 <= possible_square_index <= 63:

                    # Fixes queen movements, first diagonally, then straight.
                    if piece.type == "king":
                        if directional_counter <= 4:
                            if possible_square.default_color == current_square.default_color:
                                self.possible_moves.append(possible_square)
                        else:
                            if possible_square.x == current_square.x or possible_square.y == current_square.y:
                                self.possible_moves.append(possible_square)

                    elif piece.type == "queen":
                        if directional_counter <= 4:
                            if possible_square.default_color == current_square.default_color:
                                self.possible_moves.append(possible_square)
                        else:
                            if possible_square.x == current_square.x or possible_square.y == current_square.y:
                                self.possible_moves.append(possible_square)
                    # Makes sure the knight doesn't wrap around.
                    elif piece.type == "knight":
                        if -3 < (possible_square.x - piece.x) < 3:
                            self.possible_moves.append(possible_square)

                    elif piece.type == "pawn":
                        if -2 < (possible_square.x - piece.x) < 2:
                            if directional_counter == 1:
                                if possible_square.piece_on is None:
                                    self.possible_moves.append(possible_square)
                            else:
                                if possible_square.piece_on is not None:
                                    self.possible_moves.append(possible_square)
                                piece.capture_moves.append(possible_square)

                    # Limits bishop's movements.
                    elif piece.type == "bishop":
                        bishop_moves = get_bishop_moves(current_square=current_square, possible_square=possible_square)
                        self.possible_moves.extend(bishop_moves)

                    # Limits the rook.
                    elif piece.type == "rook":
                        rook_moves = get_rook_moves(current_square=current_square, possible_square=possible_square)
                        self.possible_moves.extend(rook_moves)

                    else:
                        self.possible_moves.append(possible_square)
        piece.moves = self.possible_moves

    def simulate_position(self):
        pass
