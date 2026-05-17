from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []

    for value in self.img:
        vertical.append(value[::-1])

    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = []

    for value in self.img[::-1]:
        horizontal.append(value)

    return Picture(horizontal)

  def negative(self):
    negativo = []

    for fila in self.img:
        nuevaFila = ""

        for caracter in fila:
            nuevaFila += self._invColor(caracter)

        negativo.append(nuevaFila)

    return Picture(negativo)

  def join(self, p):
    union = []

    for i in range(len(self.img)):
        union.append(self.img[i] + p.img[i])

    return Picture(union)

  def up(self, p):
    return Picture(p.img + self.img)

  def under(self, p):
    return Picture(self.img + p.img)
  
  def horizontalRepeat(self, n):
    resultado = self

    for i in range(n - 1):
        resultado = resultado.join(self)

    return resultado

  def rotate(self):
    """Aqui somos viciosos"""
    rotada = []

    for i in range(len(self.img[0])):
        nuevaFila = ""

        for j in range(len(self.img) - 1, -1, -1):
            nuevaFila += self.img[j][i]

        rotada.append(nuevaFila)

    return Picture(rotada)
  
  def overlay(self, p):
    """Superpone self sobre p"""
    result = []
    for i in range(len(self.img)):
        nueva_fila = ""
        for j in range(len(self.img[i])):
            c_top = self.img[i][j]
            c_bot = p.img[i][j]
            # Si el píxel de arriba es espacio, usar el de abajo
            if c_top == ' ':
                nueva_fila += c_bot
            else:
                nueva_fila += c_top
        result.append(nueva_fila)
    return Picture(result)

