from datetime import date, time, datetime
import json
class Evento:
    #Clase para crear el evento
    def __init__(self, title:str, start_date:date, start_time:time, finish_date:date, finish_time:time, type_of_event:str, arena:str, franquicia_warriors=None, randoms_warriors=None, franquicia_dragons=None, free_dragons=None, weapons=None, armors=None, extra=None):
        #Validacion para posibles errores de fechas
        if finish_date < start_date:
            raise ValueError("La fecha de fin no puede ser anterior a la de inicio")
        if finish_date == start_date and finish_time <= start_time:
            raise ValueError("La hora de fin debe ser posterior a la de inicio")

        self.title=title
        self.start_date=start_date
        self.start_time=start_time
        self.finish_date=finish_date
        self.finish_time=finish_time
        self.type_of_event=type_of_event
        self.arena=arena
        self.franquicia_warriors = list(franquicia_warriors) if franquicia_warriors else []
        self.randoms_warriors = list(randoms_warriors) if randoms_warriors else []
        self.franquicia_dragons = list(franquicia_dragons) if franquicia_dragons else []
        self.free_dragons = list(free_dragons) if free_dragons else []
        self.weapons = list(weapons) if weapons else []
        self.armors = list(armors) if armors else []
        self.extra = extra if extra else 0
        self.warriors = self.franquicia_warriors + self.randoms_warriors
        self.dragons = self.franquicia_dragons + self.free_dragons
        
    #convertir el evento en diccionario
    def to_dict(self):
        return {
            "title": self.title,
            "start_date": self.start_date.isoformat(),
            "start_time": self.start_time.isoformat(),
            "finish_date": self.finish_date.isoformat(),
            "finish_time": self.finish_time.isoformat(),
            "type_of_event": self.type_of_event,
            "arena": self.arena,
            "franquicia_warriors": self.franquicia_warriors,
            "randoms_warriors": self.randoms_warriors,
            "franquicia_dragons": self.franquicia_dragons,
            "free_dragons": self.free_dragons,
            "weapons": self.weapons,
            "armors": self.armors,
            "extra": self.extra
        }

    
    @classmethod
    def from_dict(cls, data):
        """Crea un Evento desde un diccionario"""
        return cls(
            title=data['title'],
            start_date=date.fromisoformat(data['start_date']),
            start_time=time.fromisoformat(data['start_time']),
            finish_date=date.fromisoformat(data['finish_date']),
            finish_time=time.fromisoformat(data['finish_time']),
            type_of_event=data['type_of_event'],
            arena=data['arena'],
            franquicia_warriors=data.get('franquicia_warriors', []),
            randoms_warriors=data.get('randoms_warriors', []),
            franquicia_dragons=data.get('franquicia_dragons', []),
            free_dragons=data.get('free_dragons', []),
            weapons=data.get('weapons', []),
            armors=data.get('armors', []),
            extra=data.get('extra', 0)
        )