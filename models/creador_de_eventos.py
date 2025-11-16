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
            'title':self.title,
            'start_date':self.start_date,
            'start_time':self.start_time,
            'finish_date':self.finish_date,
            'finish_time':self.finish_time,
            'type_of_event':self.type_of_event,
            'arena':self.arena,
            'dragons':self.dragons,
            'warriors':self.warriors,
            'weapons':self.weapons,
            'armors':self.armors,
            'extra':self.extra
        }
    
