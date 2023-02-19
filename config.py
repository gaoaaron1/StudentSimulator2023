WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60

#layers to represent different instances
PLAYER_LAYER = 5
SEQUENCE_LAYER2 = 4
SEQUENCE_LAYER = 3
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
    'BBBBBBBBBBBBBBBBBBBBXXXXXXXXXXXXXXXXXXBBBBBBBBBBBBBBBBBBBBBBBBXXXXX',
    'B.................RBXXXXXXXXXXXXXXXXXXBE.....................BXXXXX',
    'B..................BXXXXXXXXXXXXXXXXXXB......................BXXXXX',
    'B..................BXXXXXXXXXXXXXXXXXXB......................BXXXXX',
    'B..................BXXXXXXXXXXXXXXXXXXB......................BXXXXX',
    'B........P.........BBBBBBBBBBBBBBBBBBBB......................BXXXXX',
    'B............................................................BXXXXX',
    'B............................................................BXXXXX',
    'B..................BBBBBBBBBBBBBBBBBBBB......................BXXXXX',
    'B..................BXXXXXXXXXXXXXXXXXXB......................BXXXXX',
    'B..................BXXXXXXXXXXXXXXXXXXB......................BXXXXX',
    'B..................BXXXXXXXXXXXXXXXXXXB......................BXXXXX',
    'B..................BXXXXXXXXXXXXXXXXXXB......................BXXXXX',
    'B.................EBXXXXXXXXXXXXXXXXXXBBBBBBBB..BBBBBBBBBBBBBBXXXXX',  
    'BBBBBBBBBBBB..BBBBBBXXXXXXXXXXXXXXXXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXX',
    'XXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXX',
    'BBBBBBBBBBBB..BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB..BBBBBBBBBBBBBBBBXXX',
    'B.............BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB.................BXXX',  
    'B.............BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB.................BXXX',    
    'B..BBBBBBBBBBBBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBBBBBBBBBBBBBBBB..BXXX',
    'B..BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB..BXXX',  
    'B..BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB..BXXX',
    'B..BXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBBBBBBBBBBBBBBBBBBBBB..BXXX',
    'B..BBBBBBBBBBBBBBBXXXXXXXXXXXXXXXXXXXXXXB......................BXXX',
    'B................BXXXXXXXXXXXXXXXXXXXXXXB......................BXXX',
    'B................BXXXXXXXXXXXXXXXXXXXXXXB..BBBBBBBBBBBBBBBBBBBBBXXX',
    'B................BXXXXXXXXXXXXXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXXXXXXX',
    'B................BXXXXXXXXXXXXXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXXXXXXX',
    'B................BXXXXXXXXXXXXXXXXXXXXXXB..BXXXXXXXXXXXXXXXXXXXXXXX',
    'B................BXXXXXXXXXXXXXXXXXXBBBBB..BBBBBBBBBBBBBBBBBBBBBBBX',
    'B................BXXXXXXXXXXXXXXXXXXB............................BX',
    'B................BXXXXXXXXXXXXXXXXXXB............................BX', 
    'B................BXXXXXXXXXXXXXXXXXXB............................BX',
    'B................BBBBBBBBBBBBBBBBBBBB............................BX',
    'B................................................................BX',
    'B................................................................BX',    
    'B................BBBBBBBBBBBBBBBBBBBB............................BX',
    'B................BXXXXXXXXXXXXXXXXXXB............................BX',
    'B................BXXXXXXXXXXXXXXXXXXB............................BX',        
    'BBBBBBBBBBBBBBBBBBXXXXXXXXXXXXXXXXXXB............................BX', 
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXB............................BX',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBX',     
]