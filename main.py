# Import standard libraries
import pygame
import sys

# Import custom files
from CONST import *
from draw import *
from board import Board
from helper import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

game = Board()
selected_hexagon = None

draw_board(screen, COLOR_BOARD)

# Mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Quit the game on exit
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:    # Logic to handle when the mouse is pressed
            coordinates = pygame.mouse.get_pos()
            hexagon_position = find_closest_point(coordinates)
            selected_hexagon = highlight_selected_hexagon(screen, hexagon_position, game.board, selected_hexagon)


    pygame.display.flip()  # Update the screen
    clock.tick(60)  # Limit the frame rate to 60 FPS