# File that holds all constant values for the programm.

# Screen related
WIDTH = 1280
HEIGHT = 720

TOP_SQ_X = WIDTH * 0.1
TOP_SQ_Y = HEIGHT * 0.1

# Board related
HEXAGON_RADIUS = 40
HEXAGON_VERTICES = 6
SPACING_X = HEXAGON_RADIUS * 3
SPACING_Y = HEXAGON_RADIUS * 0.86

COLOR_BOARD = [
    ['-', '-', '-', '-', 'BLACK'],
    ['-', '-', '-', 'LIGHT_GREY', 'LIGHT_GREY'],
    ['-', '-', '-', 'WHITE', 'WHITE', "WHITE"],
    ['-', '-', 'BLACK', 'BLACK', 'BLACK', "BLACK"],
    ['-', '-', 'LIGHT_GREY', 'LIGHT_GREY', 'LIGHT_GREY', "LIGHT_GREY", 'LIGHT_GREY'],
    ['-', 'WHITE', 'WHITE', 'WHITE', 'WHITE', "WHITE", 'WHITE'],
    ['-', '-', 'BLACK', 'BLACK', 'BLACK', "BLACK", 'BLACK'],
    ['-', 'LIGHT_GREY', 'LIGHT_GREY', 'LIGHT_GREY', 'LIGHT_GREY', "LIGHT_GREY", 'LIGHT_GREY']

]

# Colors
COLOR_DICT = {'BLACK' : (209,139,71), 'LIGHT_GREY' : (232,170,111), 'WHITE' : (254,206,157)}

