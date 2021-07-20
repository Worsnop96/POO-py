class Person:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido= apellido

class Empleado(Person):
    def __init__(self, nombre, apellido, sueldo):
        super().__init__(nombre, apellido)
        self.sueldo = sueldo


