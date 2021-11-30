
WHITE =      (255, 255, 255)
GREY =       ( 64,  64,  64)
BLACK =      (  0,   0,   0)
             
RED =        (255,   0,   0)
GREEN =      (  0, 255,   0)
BLUE =       (  0,   0, 255)
             
YELLOW =     (255, 255,   0)
CYAN =       (  0, 255, 255)
PURPLE =     (127,   0, 255)
             
ORANGE =     (255, 165,   0)
PINK =       (255, 102, 255)
MAGENTA =    (255,   0, 255)

DARK_RED =   (165,   0,   0)
DARK_GREEN = (  0, 165,   0)
DARK_BLUE =  (  0,   0, 165)

LIGHT_GREEN = ( 51, 255, 51)

def get_darker(color, factor = 2/5):
    if len(color) == 4:
        darker = tuple( [int(c*factor) for c in color[:-1]] + [color[3]] )
    else:
        darker = tuple( [int(c*factor) for c in color] )

    return darker
