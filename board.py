import pygame
import math
from pieces import Rook, Knight, Bishop, King, Queen, Pawn

high_white = (250, 172, 211)
high_purple = (87, 9, 105)
off_white = (245, 243, 225)
purple = (110, 66, 166)

white_squares_color = off_white
black_squares_color = purple
high_white_squares = high_white
high_black_squares = high_purple

def format_FEN(FEN): # Transforms FEN notation into a nested list, adding a 0 for empty squares.

    FEN_rows = ""

    for char in FEN:
        if char.isdigit():
            for i in range(int(char)):
                FEN_rows += "0"
        else:
            FEN_rows += char

    FEN_rows = FEN_rows.split("/")
    new_FEN = [list(row) for row in FEN_rows]

    return new_FEN

class Board:
    def __init__(self):
        self.square_len = 100
        self.squares = []
        self.flat_squares = []
        self.all_pieces = []
        self.white_pieces = []
        self.black_pieces = []

    def draw_board(self, screen):
        for square in self.get_squares():
            pygame.draw.rect(screen, color=square.current_color, rect=square.rect)

    def create_squares(self):
        y = 0
        for c in range(8):
            x = 0
            row = []
            for r in range(8):
                square = Square(x, y, self.square_len)
                row.append(square)
                x += 1
            self.squares.append(row)
            y += 1

    def scale_sprites(self):
        for piece in self.all_pieces:
            piece.surf = pygame.transform.scale(piece.surf, (self.square_len, self.square_len))

    def create_pieces(self, position):
        FEN = format_FEN(position)

        for y, row in enumerate(FEN):
            for x, char in enumerate(row):
                if char == "0":
                    pass
                
                if char.islower():
                    color = "black"
                else:
                    color = "white"

                match char.lower():
                    case "r":
                        piece = Rook(x, y, color)
                    case "n":
                        piece = Knight(x, y, color)
                    case "b":
                        piece = Bishop(x, y, color)
                    case "q":
                        piece = Queen(x, y, color)
                    case "k":
                        piece = King(x, y, color)
                    case "p":
                        piece = Pawn(x, y, color)

                match piece.color:
                    case "white": self.white_pieces.append(piece)
                    case "black": self.black_pieces.append(piece)

                self.all_pieces.append(piece)

        self.scale_sprites()

    def update_squares(self):
        remaining_pieces = self.all_pieces
        for row in self.squares:
            for square in row:
                for piece in remaining_pieces:
                    if piece.pos == square.pos:
                        square.piece_on = piece

    def get_squares(self):
        for row in self.squares:
            for square in row:
                self.flat_squares.append(square)
        return self.flat_squares

    def reset_highlight(self):
        for square in self.get_squares():
            square.current_color = square.default_color
            square.highlight = False

    def get_color_pieces(self, color):
        match color:
            case "black": return self.black_pieces
            case "white": return self.white_pieces

    def get_color_moves(self, color):
        enemy_moves = []
        for enemy_piece in self.get_color_pieces(color):
            for move in enemy_piece.moves:
                if move not in enemy_moves:
                    enemy_moves.append(move)
        return enemy_moves


class Square:
    def __init__(self, x, y, square_size):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

        # Highlights the square for possible moves
        self.highlight = False

        # Gives the right color to the square based on position
        if (self.x + self.y) % 2 == 0:
            self.default_color = white_squares_color
            self.high_color = high_white_squares
        else:
            self.default_color = black_squares_color
            self.high_color = high_black_squares

        self.current_color = self.default_color

        # Keeps track of what piece is on the square
        self.piece_on = None

        # Pygame rect to render the square
        self.rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)

