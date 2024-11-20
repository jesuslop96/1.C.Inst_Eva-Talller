class Vehiculocarreras:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima

    def mostrar_info(self):
        print(f"El vehiculo {self.marca} del modelo {self.modelo} esta en su velocidad {self.velocidad_maxima}")

class CocheF1(Vehiculocarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_neumaticos):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_neumaticos = tipo_neumaticos

class MotoGP(Vehiculocarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_carenado):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_carenado = tipo_carenado

class Nascar(Vehiculocarreras):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_motor):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_motor = tipo_motor

coche_f1 = CocheF1("Ferrari", "SF21", 375, "Neumáticos blandos")
moto_gp = MotoGP("Yamaha", "YZF-R1", 350, "Carenado completo")
nascar = Nascar("Chevrolet", "Camaro ZL1", 320, "V8")

# Mostrar información de cada vehículo
print("Información del Coche F1:")
coche_f1.mostrar_info()

print("\nInformación de la Moto GP:")
moto_gp.mostrar_info()

print("\nInformación del Nascar:")
nascar.mostrar_info()