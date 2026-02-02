from datetime import datetime, timedelta
import json

#Funcion que a partir de una clave dada me devuelve el objeto que contiene a esta en un diccionario
def obtener_clave_por_valor(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if isinstance(valor, list):
            if valor_buscado in valor:
                return clave
        else:
            if valor == valor_buscado:
                return clave
    return None

#Regla 2
def verificar_participacion_diaria(gestor, guerreros, dragones, fecha):
    if fecha not in gestor.daily_participation:
        gestor.daily_participation[fecha] = {"guerreros": set(), "dragones": set()}

    # Verificar guerreros
    for guerrero in guerreros:
        if guerrero in gestor.franquicia_warriors and guerrero in gestor.daily_participation[fecha]["guerreros"]:
            return False, f"El guerrero {guerrero} ya participa en un evento hoy"
        
    # Verificar dragones
    for dragon in dragones:
        if dragon in gestor.franquicia_dragons and dragon in gestor.daily_participation[fecha]["dragones"]:
            return False, f"El dragón {dragon} ya participa en un evento hoy"
        
    return True, ""

#Regla 3
def verificar_dragones_con_su_guerrero(gestor, guerreros, dragones, tipo_evento):
    if tipo_evento in ["Pelea entre vikingos montados en dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
        # Verificar hermanos Brutacio y Brutilda
        brutacio_presente = "Brutacio" in guerreros
        brutilda_presente = "Brutilda" in guerreros
    
        if brutacio_presente != brutilda_presente:
            return False, "Los hermanos Brutacio y Brutilda deben ir juntos"
        else:
            for guerrero in guerreros:
                if guerrero in gestor.franquicia_warriors:
                    dragon = obtener_clave_por_valor(gestor.dragons_properties, guerrero)
                    if dragon not in dragones:
                        return False, f"El {guerrero} no puede montar si no es en {dragon}"
            return True, ""
    return True, ""

#Regla 4
def verificacion_del_cremallerus(gestor, tipo_evento, dragons, free_dragons, warriors, randoms_warriors):
    if tipo_evento in ["Pelea entre vikingos montados en dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
        total_dragons=0
        for dragon in dragons:
            if dragon == "Eructo y Guácara":
                total_dragons+=2
            else:
                count+=1
        for dragon in free_dragons.keys():
            if dragon == "Cremallerus Espantosus":
                total_dragons += free_dragons[dragon]*2
            else:
                total_dragons += free_dragons[dragon]
        total_warriors=0
        for warrior in warriors:
            total_warriors+=1
        for warrior in randoms_warriors.keys():
            total_warriors+=randoms_warriors[warrior]

        if total_warriors < total_dragons:
            return False, "No hay suficientes guerreros"
        
        if total_warriors > total_dragons:
            return False, "No hay suficientes dragones"
        
    return True, ""

#Regla 5
def verificacion_evento_ovejas(gestor, tipo_evento:str, arena:str, extra:int):
    if tipo_evento=="Competencia de encestar la oveja":
        if arena!="Playa":
            return False, f"El evento no se puede realizar en {arena}, debe realizarse en la playa"
        if extra<=0:
            return False, f"El evento no se puede realizar sin ovejas"
        return True, ""
    if tipo_evento!="Competencia de encestar la oveja" and extra>0:
        return False, f"el evento {tipo_evento} no puede utilizar ovejas"

    return True, ""
    
#Regla 6
def verificacion_evento_excursion(gestor, tipo_evento:str, arena:str):
    if tipo_evento=="Excursion para domesticar dragones":
        if arena!="Guarida de dragones":
            return False, f"El evento no se puede realizar en {arena}, debe realizarse en la Guarida de dragones"
        else:
            return True, ""
    return True, ""

#Regla 7
def verificacion_dragones_obligatorios(gestor, tipo_evento:str, free_dragons, franquicia_dragons):
    if tipo_evento in ["Pelea entre vikingos montados en dragones", "Pelea de vikingos contra dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]:
        cantidad_dragones_libres = sum(free_dragons.values())
        if cantidad_dragones_libres==0 and len(franquicia_dragons)==0:
            return False, f"Para el evento {tipo_evento} debe haber dragones"
        else:
            return True, ""
    return True, ""

#Regla 8
def verificacion_no_dragones(gestor, tipo_evento:str, free_dragons, franquicia_dragons):
    if tipo_evento == "Pelea entre vikingos":
        cantidad_dragones_libres = sum(free_dragons.values())
        if cantidad_dragones_libres>0 or len(franquicia_dragons)>0:
            return False, f"En el evento {tipo_evento} no puede haber dragones"
        else: 
            return True, ""
    return True, ""

#Regla 9
def colision_personajes(gestor, franquicia_warriors):
    if "Hippo" in franquicia_warriors and "Patán" in franquicia_warriors:
        return False, "Hippo y Patán no se llevan bien así que no pueden participar juntos en un evento"
    if "Bocón" in franquicia_warriors and "Estoico" in franquicia_warriors:
        return False, "Bocón y Estoico no se llevan bien así que no pueden participar juntos en un evento"
    return True, ""
