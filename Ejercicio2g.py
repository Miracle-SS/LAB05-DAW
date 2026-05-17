from chessPictures import *
from interpreter import draw

blanco = square
negro = square.negative()

fila_n = negro.join(blanco).horizontalRepeat(4)
# Fila de tablero empezando en blanco (claro)  
fila_b = blanco.join(negro).horizontalRepeat(4)

negras_row = (rock.negative().join(knight.negative())
    .join(bishop.negative().join(queen.negative()))
    .join(king.negative().join(bishop.negative()))
    .join(knight.negative().join(rock.negative())))
peonesN_row = pawn.negative().horizontalRepeat(8)

blancas_row = (rock.join(knight)
    .join(bishop.join(queen))
    .join(king.join(bishop))
    .join(knight.join(rock)))
peonesB_row = pawn.horizontalRepeat(8)

centro = (fila_b.under(fila_n)).under(fila_b.under(fila_n))

figura = (negras_row.overlay(fila_n)
    .under(peonesN_row.overlay(fila_b))
    .under(centro)
    .under(peonesB_row.overlay(fila_n)) 
    .under(blancas_row.overlay(fila_b)))

draw(figura)