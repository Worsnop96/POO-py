class Persona:
    def __init__(self, name="luka", surname="loki"):
        self._nombre = name
        self._apellido = surname

    def detalles(self):
        print(f"la persona se llama {self._nombre} y su apellido es {self._apellido}")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre= nombre

    def __del__(self):
        print(f"el elemento {self._nombre} con apellido {self._apellido} fue eliminado")