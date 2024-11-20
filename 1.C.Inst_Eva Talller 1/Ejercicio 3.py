import math

class Figura3D:
    def calcular_volumen(self):
        print("Método no implementado")

class Cubo(Figura3D):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        volumen = self.lado ** 3
        return volumen

class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        volumen = (4/3) * math.pi * self.radio ** 3
        return volumen

if __name__ == "__main__":

    cubo = Cubo(7)
    print(f"El volumen del cubo con lado {cubo.lado} es: {cubo.calcular_volumen()}")

    esfera = Esfera(8)
    print(f"El volumen de la esfera con radio {esfera.radio} es: {esfera.calcular_volumen()}")