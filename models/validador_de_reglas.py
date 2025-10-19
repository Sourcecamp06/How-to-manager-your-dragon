from datetime import datetime, timedelta
import json

#Regla 2
def verificar_participacion_diaria(self, guerreros, dragones, fecha):
    if fecha not in self.dayli_participation:
        self.dayli_participation[fecha] = {"guerreros": guerreros, "dragones": dragones}

    for guerrero in guerreros:
        if guerrero in self.franquicia_warriors and guerrero in self.dayli_participation[fecha]["guerreros"]:
            return False, f"El guerrero {guerrero} ya participa en un evento hoy"
        
    for dragon in dragones:
        if guerrero in self.franquicia_warriors and dragon in self.dayli_participation[fecha]["dragones"]:
            return False, f"El dragón {dragon} ya participa en un evento hoy"
    
    return True, ""

#Regla 3
def verificar_dragones_con_su_guerrero(self, guerreros, dragones, tipo_evento):
    if tipo_evento in ["Peleas entre vikingos montados en dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
        for dragon in dragones:
                if dragon in self.dragones_propiedad:
                    dueño = self.dragones_propiedad[dragon]
                    if dueño not in guerreros:
                        return False, f"El dragón {dragon} solo puede ser montado por {dueño}"