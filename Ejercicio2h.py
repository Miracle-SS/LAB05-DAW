from chessPictures import *
from interpreter import draw

N = lambda p: p.negative()
_ = None

def make_row(piezas, empieza_oscuro):
    casillas = []
    for i in range(8):
        oscuro = (i % 2 == 0) if empieza_oscuro else (i % 2 == 1)
        casilla = square.negative() if oscuro else square
        pieza = piezas[i]
        if pieza is not None:
            casillas.append(pieza.overlay(casilla))
        else:
            casillas.append(casilla)
    fila = casillas[0]
    for c in casillas[1:]:
        fila = fila.join(c)
    return fila

f8 = make_row([N(rock), _,         N(bishop), N(queen), N(king), N(bishop), N(knight), N(rock)], True)
f7 = make_row([N(pawn), N(pawn),   N(pawn),   N(pawn),  _,       _,         N(pawn),   N(pawn)], False)
f6 = make_row([_,       N(knight), _,         _,        _,       _,         _,         _      ], True)
f5 = make_row([_,       _,         _,         _,        N(pawn), _,         _,         _      ], False)
f4 = make_row([_,       _,         bishop,    _,        pawn,    _,         _,         _      ], True)
f3 = make_row([_,       _,         _,         _,        _,       knight,    _,         _      ], False)
f2 = make_row([pawn,    pawn,      pawn,      pawn,     _,       pawn,      pawn,      pawn   ], True)
f1 = make_row([rock,    knight,    bishop,    queen,    king,    _,         _,         rock   ], False)

draw(f8.under(f7).under(f6).under(f5).under(f4).under(f3).under(f2).under(f1))