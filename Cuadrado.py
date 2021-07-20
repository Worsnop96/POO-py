from Color import Color
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto*self.ancho

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)} and {Color.__str__(self)}"



cuadro= Cuadrado(55, "verde")
print(cuadro.calcularArea())