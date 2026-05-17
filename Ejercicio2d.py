from chessPictures import *
from interpreter import draw

figura = square \
    .join(square.negative()) \
    .horizontalRepeat(4)
draw(figura)