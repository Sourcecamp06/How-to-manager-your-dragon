from datetime import datetime, timedelta
import json

#Regla 2
def verificar_participacion_diaria(self, guerreros, dragones, fecha):
    if fecha not in self.dayli_participation:
        self.dayli_participation[fecha] = {"guerreros": set(), "dragones": set()}
    
    if guerrero in self.franquicia_warriors:
        for guerrero in guerreros:
            if guerrero in self.dayli_participation[fecha]["guerreros"]:
                return False, f"El guerrero {guerrero} ya participa en un evento hoy"
            
        for dragon in dragones:
            if dragon in self.dayli_participation[fecha]["dragones"]:
                return False, f"El dragón {dragon} ya participa en un evento hoy"
        
        return True, ""