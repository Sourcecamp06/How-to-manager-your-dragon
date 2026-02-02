from datetime import date, time, datetime
import json
class Evento:
    def __init__(self, title:str, start_date:date, start_time:time, finish_date:date, finish_time:time, type_of_event:str, arena:str, franquicia_warriors=None, randoms_warriors=None, franquicia_dragons=None, free_dragons=None, weapons=None, armors=None, extra=None):
        
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
        self.warriors = franquicia_warriors + randoms_warriors if franquicia_warriors or randoms_warriors else []
        self.dragons = franquicia_dragons + free_dragons if franquicia_dragons or free_dragons else []
        self.weapons=weapons if weapons else []
        self.armors=armors if armors else []
        self.extra=extra

    def to_dict(self):
        return{
            'title': self.title,
            'start_date': self.start_date.strftime("%Y-%m-%d") if self.start_date else None, 
            'start_time': self.start_time.strftime("%H:%M") if self.start_time else None,    
            'finish_date': self.finish_date.strftime("%Y-%m-%d") if self.finish_date else None,
            'finish_time': self.finish_time.strftime("%H:%M") if self.finish_time else None,
            'type_of_event': self.type_of_event,
            'arena': self.arena,
            'dragons': self.dragons,
            'warriors': self.warriors,
            'weapons': self.weapons,
            'armors': self.armors,
            'extra': self.extra
        }
    
