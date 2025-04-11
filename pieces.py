import sprites


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
                self.default_directions = [-8, -9, -7]
                self.alternate_directions = [-9, -7]
            case "black":
                self.surf = sprites.black_pawn
                self.default_directions = [+8, +9, +7]
                self.alternate_directions = [+9, +7]
        self.directions = self.default_directions


class Bishop(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "bishop"
        self.range = 7
        self.directions = [+7, +9, -7, -9]
        match self.color:
            case "white":
                self.surf = sprites.white_bishop
            case "black":
                self.surf = sprites.black_bishop


class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "knight"
        self.range = 1
        self.directions = [+6, +15, +17, +10, -6, -15, -17, -10]
        match self.color:
            case "white":
                self.surf = sprites.white_knight
            case "black":
                self.surf = sprites.black_knight


class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "rook"
        self.range = 7
        self.directions = [+8, -8, -1, +1]
        match self.color:
            case "white":
                self.surf = sprites.white_rook
            case "black":
                self.surf = sprites.black_rook


class King(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "king"
        self.range = 1
        self.directions = [+9, +7, -9, -7, +8, -8, -1, +1]
        match self.color:
            case "white":
                self.surf = sprites.white_king
            case "black":
                self.surf = sprites.black_king


class Queen(Piece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.type = "queen"
        self.range = 7
        self.directions = [+9, +7, -9, -7, +8, -8, -1, +1]
        match self.color:
            case "white":
                self.surf = sprites.white_queen
            case "black":
                self.surf = sprites.black_queen
