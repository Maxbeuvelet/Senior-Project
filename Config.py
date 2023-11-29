WIN_WIDTH = 640  # window size
WIN_HEIGHT = 480  # window size
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 4
ENEMY_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3
ENEMY_SPEED = 2

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0,)
BLUE = (0, 0, 255)
a = 0
b = 50
tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',  # Our height is 480 pixels and the each tile is 32 pixels. 480/32 = 15. So we have 15 rows
    'B..................B',  # Our width is 640 pixels. 640/32 = 20. So we have 20 columns
    'B.......E..........B',  # B represents a wall, . represents emtpy space, P represents player
    'B......bb..........B',
    'B...........b......B',
    'B..................B',
    'B........P.........B',
    'B..bbb.............B',
    'B..................B',
    'B.......b..........B',
    'B..................B',
    'B.......E..........B',
    'B..................B',
    'B.............bb...B',
    'BBBBBBBBBBBBBBBBBBBB',

]
