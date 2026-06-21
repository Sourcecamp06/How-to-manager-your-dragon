from datetime import datetime, date, time, timedelta
import json
import os
from .creador_de_eventos import Evento

class GestorEventos:
    #"Almacen" de recursos disponibles para los eventos
    def __init__(self):
        self.eventos=[]

        #Tipos de eventos
        self.type_of_events = ["Pelea entre vikingos", "Pelea entre vikingos montados en dragones", "Pelea de vikingos contra dragones", "Excursion para domesticar dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]

        #Arenas
        self.arenas = ["Arena legendaria de Berk", "Cúspide de los guerreros caídos", "Arena del jefe vikingo", "Playa", "Guarida de dragones"]

        #Guerreros de la franquicia
        self.franquicia_warriors = {"Hippo":"assets/warriors/hippo.png", "Astrid": "assets/warriors/astrid.png", "Patán": "assets/warriors/patan.png", "Patapez": "assets/warriors/patapez.png", "Brutacio": "assets/warriors/brutacio.png", "Brutilda": "assets/warriors/brutilda.png", "Estoico": "assets/warriors/estoico.png", "Bocón": "assets/warriors/bocon.png", "Valka": "assets/warriors/valka.png"}

        #Guerreros randoms
        self.randoms_warriors = {"Guerrero de Berk":5, "Guerrera de Berk":5, "Anciano de Berk":5}

        #Dragones de la franquicia
        self.franquicia_dragons = {
            "Chimuelo": "assets/dragons/chimuelo.png", 
            "Tormenta": "assets/dragons/tormenta.png", 
            "Colmillo": "assets/dragons/colmillo.png", 
            "Albondiga": "assets/dragons/albondiga.png", 
            "Eructo y Guácara": "assets/dragons/eructoyguacara.png", 
            "Gruñón": "assets/dragons/grunnon.png", 
            "Brincanubes": "assets/dragons/brincanubes.png",
            "Rompecráneos": "assets/dragons/rompecraneos.png"
        }

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
        
        # Imagenes de armas
        self.weapons_images = {
            "Escudo": "assets/weapons/escudo.png",
            "Mazo": "assets/weapons/mazo.png",
            "Espada": "assets/weapons/espada0.png",
            "Ballesta": "assets/weapons/ballesta.png",
            "Catapulta": "assets/weapons/catapulta.png"
        }

        #Armaduras
        self.armors = {
            "Casco vikingo": 10,
            "Pechera de cuero": 10,
            "Pantalon de cuero": 10, 
            "Bota de hierro": 10,
            "Cinturon de cuero":10
        }
        
        #Imagenes de armaduras
        self.armors_images = {
            "Casco vikingo": "assets/armors/casco.png",
            "Pechera de cuero": "assets/armors/pecheradecuero.png",
            "Pantalon de cuero": "assets/armors/pantalonedecuero.png",
            "Bota de hierro": "assets/armors/bota.png",
            "Cinturon de cuero": "assets/armors/cinturone.png"
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
            #Preparar datos para guardar
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
            
            #Guardar en archivo
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
            self.compilar_participacion_diaria()
            self.guardar_en_json()

            return True, f"Datos cargados desde {self.archivo_json}"
        except Exception as e:
            return False, f"Error al cargar: {e}"
    
    def auto_guardar(self):
        """Guarda automaticamente despues de cambios importantes"""
        return self.guardar_en_json()
    
    def obtener_estado_json(self):
        """Muestra como se ven los datos en JSON"""
        if self.eventos:
            return json.dumps(self.eventos[0].to_dict(), indent=2, ensure_ascii=False)
        return "No hay eventos para mostrar"


    def fecha_actual(self):
        return datetime.now().date()

    def compilar_participacion_diaria(self):
        """Reconstruye el registro de participación con los eventos actuales"""
        self.daily_participation = {}
        for evento in self.eventos:
            start = evento.start_date
            end = evento.finish_date
            delta = end - start
            
            for i in range(delta.days + 1):
                dia = start + timedelta(days=i)
                
                if dia not in self.daily_participation:
                    self.daily_participation[dia] = {"guerreros": set(), "dragones": set()}
                
                self.daily_participation[dia]["guerreros"].update(evento.franquicia_warriors)
                self.daily_participation[dia]["dragones"].update(evento.franquicia_dragons)
                