import datetime
import json
class Evento:
    def __init__(self, title:str, start_date:datetime, start_time:datetime, finish_date:datetime, finish_time:datetime, type_of_event:str, arena:str, warriors=None, dragons=None, weapons=None, armors=None, extra=None):
        self.title=title
        self.start_date=start_date
        self.start_time=start_time
        self.finish_date=finish_date
        self.finish_time=finish_time
        self.type_of_event=type_of_event
        self.arena=arena
        self.dragons=dragons if dragons else []
        self.warriors=warriors if warriors else []
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
    
