from datetime import datetime, timedelta
import json

#Funcion que a partir de una clave dada me devuelve el objeto que contiene a esta en un diccionario
def obtener_clave_por_valor(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    return None

#Regla 2
def verificar_participacion_diaria(self, guerreros, dragones, fecha):
    if fecha not in self.daily_participation:
        self.daily_participation[fecha] = {"guerreros": guerreros, "dragones": dragones}

    for guerrero in guerreros:
        if guerrero in self.franquicia_warriors and guerrero in self.daily_participation[fecha]["guerreros"]:
            return False, f"El guerrero {guerrero} ya participa en un evento hoy"
        
    for dragon in dragones:
        if guerrero in self.franquicia_warriors and dragon in self.daily_participation[fecha]["dragones"]:
            return False, f"El dragón {dragon} ya participa en un evento hoy"
    
    return True, ""

#Regla 3
def verificar_dragones_con_su_guerrero(self, guerreros, dragones, tipo_evento):
    if tipo_evento in ["Peleas entre vikingos montados en dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
        if ("Brutilda" in guerreros and "Brutacio" not in guerreros) or ("Brutacio" in guerreros and "Brutilda" not in guerreros):
            return False, f"Los hermanos Brutacio y Brutilda deben ir juntos"
        else:
            for guerrero in guerreros:
                if guerrero in ["Brutacio", "Brutilda"]:
                    dragon = "Eructo y Guácara"
                elif guerrero in self.franquicia_warriors:
                    dragon = obtener_clave_por_valor(self.dragons_properties, guerrero)
                    if dragon not in dragones:
                        return False, f"El {guerrero} no puede montar si no es en {dragon}"
            return True

#Regla 4
def verificacion_del_cremallerus(self, dragones, guerreros, tipo_evento):
    if tipo_evento in ["Peleas entre vikingos montados en dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
        count=0
        for dragon in dragones:
            if dragon == "Cremallerus Espantosus":
                count+=2
            else:
                count+=1
        if count<len(guerreros):
            return False, "No hay suficientes dragones"
        elif count>len(guerreros):
            return False, "No hay suficientes guerreros"
    return True
