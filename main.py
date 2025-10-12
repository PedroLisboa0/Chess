import pygame
from board import Board, format_FEN
from game import Game, check_capture
from saver import Saver

pygame.init()

# Sets up a screen surface
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess by Pedro Lisboa")

clock = pygame.time.Clock()
running = True

local = True # TODO Reverses the board each move

starting_position = "rnbqkbnr/ppppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
current_position = starting_position
board_setup = starting_position

board = Board()
board.create_squares()
board.create_pieces(board_setup)
board.update_squares()

game = Game(turn="white")
game.mode = "select"

saver = Saver(file="games.txt")
saver.create_game()
saver.save(starting_position)

def update_legal_moves():
    for piece in board.all_pieces:
        game.get_moves(piece=piece, squares=board.get_squares())
    # Limits the king so it cannot enter check
    # TODO vou ter que fazer uma "simulação" da posição caso tal lance aconteça mesmo. Acho inclusive que o melhor
    # TODO é fazer um novo arquivo e classe Simulators



def handle_click(mouse_position):
    for square in board.get_squares():
            if square.rect.collidepoint(mouse_position) == False:
                continue

            if game.mode == "move" and (square in game.selected_piece.moves):
                check_capture(new_square=square, pieces=board.all_pieces,
                    white_pieces=board.white_pieces, black_pieces=board.black_pieces)
                game.move_piece(square)
                game.change_turn()
                board.update_highlight(reset=True)
                update_legal_moves()
                game.unselect()
                game.mode = "select"
                return
            
            elif square.piece_on != None:
                game.selected_square = square
                game.selected_piece = square.piece_on
                board.update_highlight(reset=True)
                if game.selected_piece.color == game.turn:
                    for possible_square in game.selected_piece.moves:
                        possible_square.highlight = True
                    board.update_highlight()
                    game.mode = "move"
                return            
                
            elif square.piece_on == None:
                game.unselect()
                board.update_highlight(reset=True)
                game.mode = "select"
                return


update_legal_moves()

while running:
    # Checks if the user closed the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_r:
                    print("Mode", game.mode)
                    print("Turn", game.turn)
                    print("s-square", game.selected_square)
                    print("s-piece", game.selected_piece)

        # Moves the pieces (or tries to lol)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            handle_click(mouse_position)


    # Renders the board
    board.draw_board(screen=screen)

    # Renders the pieces and codes the new FEN
    new_FEN = ""
    for row in board.squares:
        for square in row:
            if square.piece_on is not None:
                screen.blit(source=square.piece_on.surf, dest=(square.piece_on.x * board.square_len,
                                                               square.piece_on.y * board.square_len))
                new_FEN += square.piece_on.fen_notation
            else:
                new_FEN += "0"
        new_FEN += "/"

    if current_position != new_FEN:
        current_position = new_FEN
        saver.save(format_FEN(current_position))

    # Updates the screen
    pygame.display.flip()

pygame.quit()
