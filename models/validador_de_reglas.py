from datetime import datetime, timedelta
import json

#Funcion que a partir de una clave dada me devuelve el objeto que contiene a esta en un diccionario
def obtener_clave_por_valor(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor in valor_buscado:
            return clave
    return None

#Regla 2
def verificar_participacion_diaria(self, guerreros, dragones, fecha):
    if fecha not in self.daily_participation:
        self.daily_participation[fecha] = {"guerreros": set(), "dragones": set()}

    # Verificar guerreros
    for guerrero in guerreros:
        if guerrero in self.franquicia_warriors and guerrero in self.daily_participation[fecha]["guerreros"]:
            return False, f"El guerrero {guerrero} ya participa en un evento hoy"
        
    for dragon in dragones:
        if dragon in self.franquicia_dragons and dragon in self.daily_participation[fecha]["dragones"]:
            return False, f"El dragón {dragon} ya participa en un evento hoy"
        
    # Si todo está bien, agregar a la participación diaria
    self.daily_participation[fecha]["guerreros"].update(guerreros)
    self.daily_participation[fecha]["dragones"].update(dragones)
    
    return True, ""

#Regla 3
def verificar_dragones_con_su_guerrero(self, guerreros, dragones, tipo_evento):
    if tipo_evento in ["Pelea entre vikingos montados en dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
        # Verificar hermanos Brutacio y Brutilda
        brutacio_presente = "Brutacio" in guerreros
        brutilda_presente = "Brutilda" in guerreros
    
        if brutacio_presente != brutilda_presente:
            return False, "Los hermanos Brutacio y Brutilda deben ir juntos"
        else:
            for guerrero in guerreros:
                if guerrero in self.franquicia_warriors:
                    dragon = obtener_clave_por_valor(self.dragons_properties, guerrero)
                    if dragon not in dragones:
                        return False, f"El {guerrero} no puede montar si no es en {dragon}"
            return True, ""

#Regla 4
def verificacion_del_cremallerus(self, dragones, guerreros, tipo_evento):
    if tipo_evento in ["Pelea entre vikingos montados en dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
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
    return True, ""

#Regla 5
def verificacion_evento_ovejas(self, tipo_evento:str, arena:str, extra:int):
    if tipo_evento=="Competencia de encestar la oveja":
        if arena!="Playa":
            return False, f"El evento no se puede realizar en {arena}, debe realizarse en la playa"
        if extra<=0:
            return False, f"El evento no se puede realizar con {extra} ovejas"
    else:
        return True, ""
    
#Regla 6
def verificacion_evento_excursion(self, tipo_evento:str, arena:str):
    if tipo_evento=="Excursion para domesticar dragones":
        if arena!="Guarida de dragones":
            return False, f"El evento no se puede realizar en {arena}, debe realizarse en la Guarida de dragones"
    else:
        return True, ""