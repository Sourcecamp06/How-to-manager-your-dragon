from datetime import datetime, timedelta
import json

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
        self.randoms_warriors = {"Guerreros de Berk":5, "Guerreras de Berk":5, "Ancianos de Berk":5}

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
            "Escudos": 8,
            "Mazos": 8, 
            "Espadas": 8,
            "Ballestas": 3,
            "Catapulta": 1
        }

        #Armaduras
        self.armors = {
            "Cascos vikingos": 10,
            "Pecheras de cuero": 10,
            "Pantalones de cuero": 10, 
            "Botas de hierro": 10,
            "Cinturones de cuero":10
        }

        #ovejas
        self.ovejas = 20

        #Registro de participacion diaria
        self.daily_participation = {}

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
    def duration(start_date:datetime, start_time:datetime, finish_date:datetime, finish_time:datetime):
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


    def fecha_actual(self):
        return datetime.now().date()


