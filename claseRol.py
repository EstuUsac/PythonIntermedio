from enum import Enum

class Rol(Enum):
    ADMIN = "Administrador"
    USUARIO = "Usuario"
    INVITADO = "Invitado"
    ANONIMO = "Anonimo"
    DESCONOCIDO = "Desconocido"

    def __str__(self):
        return self.value
