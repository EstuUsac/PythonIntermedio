from claseRol import Rol
from claseLugar import Lugar

class Persona:
    def __init__(self, nombre, edad, rol, foto):
        self.nombre = nombre
        self.edad = edad
        self.rol = rol
        self.foto = r"C:\Users\estua\Downloads\estuardo.jpg"
        self.lugares = []  
    
    def agregar_lugar(self, lugar: Lugar):
        self.lugares.append(lugar)
    
    def __str__(self):
        lugares_str = "\n".join([f"{lugar.nombre}, {lugar.direccion}" for lugar in self.lugares])
        return (f"La persona: {self.nombre}," f"con foto tipo {self.foto.split('.')[-1].upper()} ubicada en {self.foto}," f"y rol de {self.rol.value}, tiene los siguientes lugares:\n{lugares_str}")
