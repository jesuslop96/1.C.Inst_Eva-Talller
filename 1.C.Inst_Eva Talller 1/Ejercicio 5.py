class Mascota:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def mostrar_info(self):
        print(f"La mascota: {self.nombre} tiene la edad {self.edad} y su especie es {self.especie}")

class Perro(Mascota):
    def __init__(self, nombre, edad, especie, raza):
        super().__init__(nombre, edad, especie)
        self.raza = raza

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Raza: {self.raza}")

    def ladrar(self):
        print("Guau, guau")

class Gato(Mascota):
    def __init__(self, nombre, edad, especie, color):
        super().__init__(nombre, edad, especie)
        self.color = color

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Color: {self.color}")

    def maullar(self):
        print("Miau")


class Loro(Mascota):
    def __init__(self, nombre, edad, especie, tipo_pico):
        super().__init__(nombre, edad, especie)
        self.tipo_pico = tipo_pico

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"Tipo de pico: {self.tipo_pico}")

    def canto(self):
        print("Pasa me la materia")

# Ejemplo de uso
perro1 = Perro("Rex", 5, "Perro", "Pastor Alemán")
gato1 = Gato("Miau", 3, "Gato", "Blanco")
loro1 = Loro("Polly", 2, "Loro", "Curvo")

print("Información del Perro:")
perro1.mostrar_info()
perro1.ladrar()

print("\nInformación del Gato:")
gato1.mostrar_info()
gato1.maullar()

print("\nInformación del Loro:")
loro1.mostrar_info()
loro1.canto()