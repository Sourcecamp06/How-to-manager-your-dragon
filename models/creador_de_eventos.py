from datetime import datetime, timedelta
import json
class Evento:
    def __init__(self, title, start_date, start_time, duration, type_of_event="", arena="", warriors=None, dragons=None, weapons=None, armors=None):
        self.title=title
        self.start_date=start_date
        self.start_time=start_time
        self.duration=duration
        self.type_of_event=type_of_event
        self.arena=arena
        self.dragons=dragons if dragons else []
        self.warriors=warriors if warriors else []
        self.weapons=weapons if weapons else []
        self.armors=armors if armors else []

    def to_dict(self):
        return{
            'title':self.title,
            'start_date':self.start_date,
            'start_time':self.start_time,
            'duration':self.duration,
            'type_of_event':self.type_of_event,
            'arena':self.arena,
            'dragons':self.dragons,
            'warriors':self.warriors,
            'weapons':self.weapons,
            'armors':self.armors
        }
    
