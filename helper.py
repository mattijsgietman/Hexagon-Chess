import math

from CONST import *

def find_closest_point(pos):
    min_distance = float('inf')
    closest_point = None

    for point in ALL_POS:   # Loop over all points on the screen
        x1, y1 = point
        x2, y2 = pos
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)   # Find distance between clicked point and target point
        if distance < min_distance:
            min_distance = distance
            closest_point = point

    if closest_point in HEXAGON_POS:    # Check if closest point is on a hexagon
        return closest_point            # Return closest point if it is a hexagon
    else:
        return None                     # Else return None

def find_hexagon(pos):
    try:
        return POS_TO_TILE[pos]         # Returns the index of the hexagon
    except:
        return None                     # Else returns None

