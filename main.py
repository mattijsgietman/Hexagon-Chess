# Import standard libraries
import pygame
import sys

# Import custom files
from CONST import *
from draw import *
from board import Board
from helper import *
from move import Move

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# Initialize the first game state
game = Board()
game.hexagon_setup()
game.piece_setup()
board = game.board

selected_hexagon = (None, None)     # Start with no squares selected
selected_piece = None               # Start with no piece selected
turn = 'white'                      # White starts the game

draw_board(screen, COLOR_BOARD)     # Draw the board
draw_pieces(screen, game.board)     # Draw the pieces


# Mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Quit the game on exit
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:    # Logic to handle when the mouse is pressed
            coordinates = pygame.mouse.get_pos()                    # Get the mouse position
            hexagon_position = find_closest_point(coordinates)      # Get the position closest to the selected hexagon
            selected_hexagon = selected_hexagons(hexagon_position, selected_hexagon, board, turn, screen)       # Select the correct hexagon
            selected_piece =  None if selected_hexagon[0] is None else board[selected_hexagon[0][1]][selected_hexagon[0][0]].piece     # Select the piece that was clicked on

            if selected_piece is not None and selected_hexagon[1] is not None:                                  # If this is the case make a move
                move = Move(selected_piece, selected_hexagon[0], selected_hexagon[1])
                make_move(board, move, selected_piece)
                selected_hexagon = deselect_hexagons(screen, board)
                turn = switch_turns(turn)

            draw_selected_hexagons(screen, selected_hexagon)                                                    # Visualize the selected hexagon
            draw_pieces(screen, board)                                                                          # Draw the pieces over the hexagon

    pygame.display.flip()  # Update the screen
    clock.tick(10)  # Limit the frame rate to 10 FPS


