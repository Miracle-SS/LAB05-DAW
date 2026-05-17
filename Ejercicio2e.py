from chessPictures import *
from interpreter import draw

figura = square.negative() \
    .join(square) \
    .horizontalRepeat(4)
draw(figura)