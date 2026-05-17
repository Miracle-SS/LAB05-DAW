from chessPictures import *
from interpreter import draw

arriba = knight \
    .join(knight.negative())
abajo = knight.verticalMirror().negative() \
    .join(knight.verticalMirror())
figura = arriba.under(abajo)
draw(figura)