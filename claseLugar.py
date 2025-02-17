class Lugar:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
    
    def __str__(self):
        return f"{self.nombre} ({self.direccion})"
