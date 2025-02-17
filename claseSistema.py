from clasePersona import Persona

class Sistema:
    def __init__(self):
        self.personas = []
    
    def agregar_persona(self, persona: Persona):
        self.personas.append(persona)
    
    def __str__(self):
        return "\n".join([str(persona) for persona in self.personas])
