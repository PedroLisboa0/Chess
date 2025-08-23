import pygame
from board import Board
from game import Game, check_capture, change_turn, get_enemy_color

pygame.init()

# Sets up a screen surface
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess by Pedro Lisboa")

clock = pygame.time.Clock()
running = True

board_setup = None

board = Board()
board.create_squares()
board.create_pieces(board_setup)
board.update_squares()

game = Game()
selected_piece = None
selected_square = None
mode = "select"
turn = "white"


def update_legal_moves():
    for piece in board.all_pieces:
        game.get_moves(piece=piece, squares=board.get_squares())
    # Limits the king so it cannot enter check
    # TODO vou ter que fazer uma "simulação" da posição caso tal lance aconteça mesmo. Acho inclusive que o melhor
    # TODO é fazer um novo arquivo e classe Simulator


update_legal_moves()

while running:
    # Checks if the user closed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Moves the pieces (or tries to lol)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            # For some reason, I have to loop through all the 8 lists in boards.squares, it doesn't work properly
            # if I loop through the flat list.
            for row in board.squares:
                for square in row:

                    if (square.rect.collidepoint(mouse_position) and square.piece_on is not None
                            and mode == "select" and square.piece_on.moves != []):
                        selected_square = square
                        selected_piece = square.piece_on
                        if selected_piece.color == turn:
                            # Highlights all possible squares
                            for possible_square in selected_piece.moves:
                                possible_square.highlight = True
                                possible_square.current_color = possible_square.high_color
                            mode = "move"

                    elif square.rect.collidepoint(mouse_position) and mode == "move" and square in selected_piece.moves:
                        check_capture(new_square=square, pieces=board.all_pieces,
                                      white_pieces=board.white_pieces, black_pieces=board.black_pieces)
                        selected_piece.update_position(square.pos)
                        square.piece_on = selected_piece
                        selected_square.piece_on = None
                        turn = change_turn(turn)
                        board.reset_highlight()
                        update_legal_moves()
                        mode = "select"

    # Render the board
    board.draw_board(screen=screen)

    # Renders the pieces
    for row in board.squares:
        for square in row:
            if square.piece_on is not None:
                screen.blit(source=square.piece_on.surf, dest=(square.piece_on.x * board.square_len,
                                                               square.piece_on.y * board.square_len))

    # Updates the screen
    pygame.display.flip()

pygame.quit()
