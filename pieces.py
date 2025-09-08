import sprites

piece_directions = {
    "pawn_default": [-8, -9, -7],
    "pawn_capture": [-9, -7],
    "bishop":[+7, +9, -7, -9],
    "knight":[+6, +15, +17, +10, -6, -15, -17, -10],
    "rook":[+8, -8, -1, +1],
    "king":[+9, +7, -9, -7, +8, -8, -1, +1]
}

class Piece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.color = color
        self.already_moved = False
        self.moves = []

    def update_position(self, new_pos: tuple):
        new_x, new_y = new_pos
        self.pos = new_pos
        self.x = new_x
        self.y = new_y
        self.already_moved = True


class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "pawn"
        self.range = 2
        self.capture_moves = []
        match self.color:
            case "white":
                self.surf = sprites.white_pawn
                self.default_directions = piece_directions["pawn_default"]
                self.capture_directions = piece_directions["pawn_capture"]
                self.fen_notation = "p"
            case "black":
                self.surf = sprites.black_pawn
                self.default_directions = [x*-1 for x in piece_directions["pawn_default"]]
                self.capture_directions = [x*-1 for x in piece_directions["pawn_capture"]]
                self.fen_notation = "P"
        self.directions = self.default_directions


class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "bishop"
        self.range = 7
        self.directions = piece_directions["bishop"]
        match self.color:
            case "white":
                self.surf = sprites.white_bishop
                self.fen_notation = "b"
            case "black":
                self.surf = sprites.black_bishop
                self.fen_notation = "B"

class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "knight"
        self.range = 1
        self.directions = piece_directions["knight"]
        match self.color:
            case "white":
                self.surf = sprites.white_knight
                self.fen_notation = "n"
            case "black":
                self.surf = sprites.black_knight
                self.fen_notation = "N"


class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "rook"
        self.range = 7
        self.directions = piece_directions["rook"]
        match self.color:
            case "white":
                self.surf = sprites.white_rook
                self.fen_notation = "r"
            case "black":
                self.surf = sprites.black_rook
                self.fen_notation = "R"


class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "king"
        self.range = 1
        self.directions = piece_directions["king"]
        match self.color:
            case "white":
                self.surf = sprites.white_king
                self.fen_notation = "k"
            case "black":
                self.surf = sprites.black_king
                self.fen_notation = "K"


class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "queen"
        self.range = 7
        self.directions = piece_directions["king"]
        match self.color:
            case "white":
                self.surf = sprites.white_queen
                self.fen_notation = "q"
            case "black":
                self.surf = sprites.black_queen
                self.fen_notation = "Q"
