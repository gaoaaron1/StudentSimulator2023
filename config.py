WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60

#layers to represent different instances
PLAYER_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255) 
WHITE = (255, 255, 255)

#B represents walls and 
# ... represents paths
# P represents player
tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B..................B',
    'B..................B',
    'B....BBB...........B',
    'B..................B',
    'B........P.........B',
    'B..................B',
    'B..................B',
    'B.....BBB..........B',
    'B.......B..........B',
    'B.......B..........B',
    'B..................B',
    'B..................B',
    'B..................B',  
    'BBBBBBBBBBBB..BBBBBB',
    'BBBBBBBBBBBB..BBBBBB',
    'B..................B',
    'B..................B',
    'B..................B',  
    'BBBBBBBBBBBBBBBBBBBB',    
]