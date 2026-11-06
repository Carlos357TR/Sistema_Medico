class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo = codigo
        self._nombre = nombre
        self._edad = edad

    #Getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    #Setters   
    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    def resumen(self):
        return f"{self._codigo} - {self._edad} - {self._nombre}"