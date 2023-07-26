# Import standard libraries
import pygame
import sys

# Import custom files
from CONST import *
from draw import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#draw_board(screen, [1, 2], (TOP_SQ_X, TOP_SQ_Y))

draw_board(screen, COLOR_BOARD)


# Mainloop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    pygame.display.flip()  # Update the screen
    clock.tick(60)  # Limit the frame rate to 60 FPS