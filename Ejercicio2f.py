from chessPictures import *
from interpreter import draw

fila1 = square \
    .join(square.negative()) \
    .horizontalRepeat(4)
fila2 = square.negative() \
    .join(square) \
    .horizontalRepeat(4)
figura = fila1 \
    .under(fila2) \
    .under(fila1) \
    .under(fila2)
draw(figura)