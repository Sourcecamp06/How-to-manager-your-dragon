from datetime import datetime, timedelta
import json

#Regla 2
def verificar_participacion_diaria(self, guerreros, dragones, fecha):
        """Verifica que guerreros y dragones no estén en otro evento ese día"""
        if fecha not in self.participacion_diaria:
            self.participacion_diaria[fecha] = {"guerreros": set(), "dragones": set()}
        
        for guerrero in guerreros:
            if guerrero in self.participacion_diaria[fecha]["guerreros"]:
                return False, f"El guerrero {guerrero} ya participa en un evento hoy"
                
        for dragon in dragones:
            if dragon in self.participacion_diaria[fecha]["dragones"]:
                return False, f"El dragón {dragon} ya participa en un evento hoy"
            
        return True, ""