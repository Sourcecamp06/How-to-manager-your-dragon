from datetime import datetime, date, time
import json
import os
from .creador_de_eventos import Evento

class GestorEventos:
    def __init__(self):
        self.eventos=[]

        #Tipos de eventos
        self.type_of_events = ["Pelea entre vikingos", "Pelea entre vikingos montados en dragones", "Pelea de vikingos contra dragones", "Excursion para domesticar dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]

        #Arenas
        self.arenas = ["Arena legendaria de Berk", "Cúspide de los guerreros caídos", "Arena del jefe vikingo", "Playa", "Guarida de dragones"]

        #Guerreros de la franquicia
        self.franquicia_warriors = ["Hippo", "Astrid", "Patán", "Patapez", "Brutacio", "Brutilda", "Estoico", "Bocón", "Valka"]

        #Guerreros randoms
        self.randoms_warriors = {"Guerrero de Berk":5, "Guerrera de Berk":5, "Anciano de Berk":5}

        #Dragones de la franquicia
        self.franquicia_dragons = ["Chimuelo", "Tormenta", "Colmillo", "Albondiga", "Eructo y Guácara", "Rompecráneos", "Gruñón", "Brincanubes"]

        #Dragones libres
        self.free_dragons = {
            "Terror Terrible": 5,
            "Nadder Mortal": 3,
            "Gronckle": 2,
            "Cremallerus Espantosus": 3,
            "Monstrous Nightmare": 3,
            "Light Fury": 1,
            "Thunderdrum": 1
        }

        #Asignacion de dragones-duenios
        self.dragons_properties = {
            "Chimuelo": "Hippo",
            "Tormenta": "Astrid", 
            "Albondiga": "Patapez",
            "Gruñón": "Bocón",
            "Eructo y Guácara": ["Brutacio", "Brutilda"],
            "Colmillo": "Patán",
            "Rompecráneos": "Estoico",
            "Brincanubes": "Valka"
        }

        #Armas
        self.weapons = {
            "Escudo": 8,
            "Mazo": 8, 
            "Espada": 8,
            "Ballesta": 3,
            "Catapulta": 1
        }

        #Armaduras
        self.armors = {
            "Casco vikingo": 10,
            "Pechera de cuero": 10,
            "Pantalone de cuero": 10, 
            "Bota de hierro": 10,
            "Cinturone de cuero":10
        }

        #ovejas
        self.ovejas = 20

        #Registro de participacion diaria
        self.daily_participation = {}

        self.archivo_json = "data/eventos.json"
        if not os.path.exists("data"):
            os.makedirs("data")

        self.cargar_desde_json()

    def verificar_recursos_disponibles(self, recursos_solicitados):
        pass

    #Verificacion de si la arena esta disponible en la fecha y hora especificadas
    def verificar_disponibilidad_arena(self, arena, new_start_date, new_start_time, new_finish_date, new_finish_time):
        new_start = datetime.combine(new_start_date, new_start_time)
        new_end = datetime.combine(new_finish_date, new_finish_time)

        for evento in self.eventos:
            if evento.arena == arena:
                actual_start = datetime.combine(evento.start_date, evento.start_time)
                actual_end = datetime.combine(evento.finish_date, evento.finish_time)

                if new_start < actual_end and new_end > actual_start:
                    return False, "La arena no esta disponible en este horario"

        return True, ""

    #Duracion de eventos
    def duration(self, start_date:datetime, start_time:datetime, finish_date:datetime, finish_time:datetime):
        start = datetime.combine(start_date, start_time)
        finish = datetime.combine(finish_date, finish_time)
        duration = abs(finish - start)
        duration = duration.total_seconds()/60
        return duration

    #Buscar hueco
    def recomendar_fecha(self, arena, start_date:datetime, start_time:datetime, finish_date:datetime, finish_time:datetime):
        actual_duration = self.duration(start_date, start_time, finish_date, finish_time)
        events_list=[]
        for evento in self.eventos:
            if arena == evento.arena:
                events_list.append(evento)
        for i in range(len(events_list)):
            for j in range(i, len(events_list)):
                if events_list[i].start_date > events_list[j].start_date:
                    events_list[i], events_list[j] = events_list[j], events_list[i]
        actual_inicio= datetime.combine(start_date, start_time) 

        for i in range(1, len(events_list)):
            nuevo_inicio = datetime.combine(events_list[i].start_date, events_list[i].start_time)
            if self.duration(events_list[i-1].finish_date, events_list[i-1].finish_time, events_list[i].start_date, events_list[i].start_time) >= actual_duration and  nuevo_inicio >= actual_inicio:
                return f"Fecha recomendada: {events_list[i-1].finish_date} a las {events_list[i-1].finish_time}"
        else: 
            return f"Fecha recomendada: {events_list[len(events_list)-1].finish_date} a las {events_list[len(events_list)-1].finish_time}"

    
    def guardar_en_json(self):
        """Guarda todos los eventos y recursos actuales en JSON"""
        try:
            # Preparar datos para guardar
            datos = {
                "eventos": [evento.to_dict() for evento in self.eventos],
                "recursos_actuales": {
                    "randoms_warriors": self.randoms_warriors,
                    "free_dragons": self.free_dragons,
                    "weapons": self.weapons,
                    "armors": self.armors,
                    "ovejas": self.ovejas
                },
                "daily_participation": {
                    str(fecha): {
                        "guerreros": list(datos["guerreros"]),
                        "dragones": list(datos["dragones"])
                    }
                    for fecha, datos in self.daily_participation.items()
                },
                "fecha_ultima_actualizacion": datetime.now().isoformat()
            }
            
            # Guardar en archivo
            with open(self.archivo_json, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            
            return True, f"Datos guardados en {self.archivo_json}"
        except Exception as e:
            return False, f"Error al guardar: {e}"
    
    def cargar_desde_json(self):
        """Carga eventos y recursos desde JSON"""
        try:
            if not os.path.exists(self.archivo_json):
                return False, f"Archivo {self.archivo_json} no existe"
            
            with open(self.archivo_json, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            # Restaurar eventos
            self.eventos = []
            for evento_data in datos.get("eventos", []):
                self.eventos.append(Evento.from_dict(evento_data))

            # Restaurar recursos
            recursos = datos.get("recursos_actuales", {})
            self.randoms_warriors = recursos.get("randoms_warriors", self.randoms_warriors)
            self.free_dragons = recursos.get("free_dragons", self.free_dragons)
            self.weapons = recursos.get("weapons", self.weapons)
            self.armors = recursos.get("armors", self.armors)
            self.ovejas = recursos.get("ovejas", self.ovejas)
            
            # Restaurar participación diaria
            daily_data = datos.get("daily_participation", {})
            self.daily_participation = {}
            for fecha_str, datos_dia in daily_data.items():
                fecha = date.fromisoformat(fecha_str)
                self.daily_participation[fecha] = {
                    "guerreros": set(datos_dia["guerreros"]),
                    "dragones": set(datos_dia["dragones"]),
                }

            return True, f"Datos cargados desde {self.archivo_json}"
        except Exception as e:
            return False, f"Error al cargar: {e}"
    
    def auto_guardar(self):
        """Guarda automáticamente después de cambios importantes"""
        return self.guardar_en_json()
    
    def obtener_estado_json(self):
        """Muestra cómo se ven los datos en JSON (para debugging)"""
        if self.eventos:
            return json.dumps(self.eventos[0].to_dict(), indent=2, ensure_ascii=False)
        return "No hay eventos para mostrar"


    def fecha_actual(self):
        return datetime.now().date()


