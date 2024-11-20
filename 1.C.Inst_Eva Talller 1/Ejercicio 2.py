class EmpleadoHospital:
    def __init__(self, nombre, id, departamento, salario_base):
        self.nombre = nombre
        self.id = id
        self.departamento = departamento
        self.salario_base = salario_base

    def mostrar_info(self):
        print(f"El medico {self.nombre} su Identificacion es {self.id} es del departamento {self.departamento} y tiene un salario de {self.salario_base}")

class Medico(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, especialidad, num_pacientes):
        super().__init__(nombre, id, departamento, salario_base)
        self.especialidad = especialidad
        self.num_pacientes = num_pacientes

class Enfermero(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, turno, planta):
        super().__init__(nombre, id, departamento, salario_base)
        self.turno = turno
        self.planta = planta

class Practicante(EmpleadoHospital):
    def __init__(self, nombre, id, departamento, salario_base, semestre_estudio):
        super().__init__(nombre, id, departamento, salario_base)
        self.semestre_estudio = semestre_estudio

medico1 = Medico("Dr. Juan Pérez", "001", "Cardiología", 5000, "Cardiología", 120)
enfermero1 = Enfermero("Sara", "30023", "Pediatría", 2500000, "Nocturno", "Planta 12")
practicante1 = Practicante("Katherine", "12501", "Urgencias", 1700000, "8vo")

print("Información del Médico:")
medico1.mostrar_info()

print("\nInformación del Enfermero 1:")
enfermero1.mostrar_info()

print("\nInformación del Practicante 1:")
practicante1.mostrar_info()