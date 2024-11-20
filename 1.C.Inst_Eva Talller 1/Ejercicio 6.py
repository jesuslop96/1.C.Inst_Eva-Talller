class ProductoElectronico:
    def __init__(self, nombre, precio, marca):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca

    def mostrar_info(self):
        print(f"El producto: {self.nombre} es de la marca {self.marca} y tiene el valor de {self.precio}")

class TelefonoMovil(ProductoElectronico):
    def __init__(self, nombre, precio, marca, capacidad_bateria):
        super().__init__(nombre, precio, marca)
        self.capacidad_bateria = capacidad_bateria

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de batería: {self.capacidad_bateria} mAh")

class Laptop(ProductoElectronico):
    def __init__(self, nombre, precio, marca, tamano_pantalla):
        super().__init__(nombre, precio, marca)
        self.tamano_pantalla = tamano_pantalla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tamaño de pantalla: {self.tamano_pantalla} pulgadas")

class Televisor(ProductoElectronico):
    def __init__(self, nombre, precio, marca, resolucion):
        super().__init__(nombre, precio, marca)
        self.resolucion = resolucion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Resolución: {self.resolucion}")


telefono = TelefonoMovil("iPhone 14", 999, "Apple", 3110)
laptop = Laptop("MacBook Pro", 2399, "Apple", 16)
televisor = Televisor("Samsung 4K", 899, "Samsung", "4K UHD")

print("Información del Teléfono Móvil:")
telefono.mostrar_info()

print("\nInformación de la Laptop:")
laptop.mostrar_info()

print("\nInformación del Televisor:")
televisor.mostrar_info()