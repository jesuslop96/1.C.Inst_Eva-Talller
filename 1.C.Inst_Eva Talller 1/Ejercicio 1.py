class Materialbiblioteca:
    def __init__(self, titulo, autor, codigo, disponible = True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El material {self.titulo} a sido prestado")
        else:
            print(f"El material {self.titulo} no se encuentra disponible para prestamo")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"El material '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El material '{self.titulo}' ya está disponible.")

    def mostrar_info(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        print(f"El material {self.titulo} del autor {self.autor} con el codigo {self.codigo} tiene el estado {disponibilidad}")

class Libro(Materialbiblioteca):
    def __init__(self, titulo, autor, codigo, numero_paginas, genero, disponible = True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_paginas = numero_paginas
        self.genero = genero

class Revista(Materialbiblioteca):
    def __init__(self, titulo, autor, codigo, numero_edicion, fecha_publicacion, disponible = True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

class Diccionario(Materialbiblioteca):
    def __init__(self, titulo, autor, codigo, numero_volumen, disponible = True):
        super().__init__(titulo, autor, codigo, disponible)
        self.numero_volumen = numero_volumen

libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "001", 417, "Realismo mágico")
revista1 = Revista("National Geographic", "Varios autores", "002", 345, "2024-11-01")
diccionario1 = Diccionario("Diccionario Compact", "Larousse", "2155634", "VII")

print("Información del libro:")
libro1.mostrar_info()
print()

print("Información de la revista:")
revista1.mostrar_info()
print()

print("Información del diccionario:")
diccionario1.mostrar_info()
print()

print("Préstamo y devolución del libro:")
libro1.prestar()
libro1.mostrar_info()
libro1.devolver()
libro1.mostrar_info()