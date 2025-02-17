from clasePersona import Persona
from claseLugar import Lugar
from claseSistema import Sistema
from claseRol import Rol

def main():
    lugar1 = Lugar("USAC", "Zona 12")
    lugar2 = Lugar("Casa", "Zona 5")
    lugar3 = Lugar("Trabajo", "Zona 10")
    lugar4 = Lugar("Gym", "Zona 4")
    lugar5 = Lugar("Centro Comercial", "Zona 9")
    lugar6 = Lugar("Parque", "Zona 14")
    
    # Estuardo
    persona1 = Persona("Estuardo Ramirez", 18, Rol.ADMIN, r"C:\Users\estua\Downloads\estuardo.jpg")
    persona1.agregar_lugar(lugar1)
    persona1.agregar_lugar(lugar2)
    persona1.agregar_lugar(lugar3)

    # Gabriel
    persona2 = Persona("Gabriel Arias", 18, Rol.INVITADO, r"C:\Users\gabriel\Downloads\gabriel.jpg")
    persona2.agregar_lugar(lugar4)
    persona2.agregar_lugar(lugar5)
    persona2.agregar_lugar(lugar6)

    sistema = Sistema()
    sistema.agregar_persona(persona1)
    sistema.agregar_persona(persona2)

    print(sistema)

if __name__ == "__main__":
    main()
