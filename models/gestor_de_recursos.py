from datetime import datetime, timedelta
import json

class GestorEventos:
    def __init__(self):
        self.eventos=[]

        #Tipos de eventos
        self.type_of_events = ["Pelea entre vikingos", "Pelea entre vikingos montados en dragones", "Pelea de vikingos contra dragones", "Excursion para domesticar dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]

        #Arenas
        self.arenas = ["Arena principal", "Arena secundaria1", "Arena secundaria2", "Playa", "Guarida de dragones"]

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

    def fecha_actual(self):
        return datetime.now().strftime("%Y-%m-%d")

