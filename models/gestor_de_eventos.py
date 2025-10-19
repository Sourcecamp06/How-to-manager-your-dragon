from datetime import datetime, timedelta
import json

class GestorEventos:
    def __init__(self):
        self.event=[]

        #Tipos de eventos
        self.type_of_events = ["Peleas entre vikingos", "Peleas entre vikingos montados en dragones", "Peleas de vikingos contra dragones", "Excursiones para domesticar dragones", "Competencia de encestar la oveja", "Entrenamiento de vuelo"]

        #Arenas
        self.arenas = ["Arena principal", "Arena secundaria1", "Arena secundaria2", "Playa", "Guarida de dragones"]

        #Guerreros de la franquicia
        self.franquicia_warriors = ["Hippo", "Astrid", "Patán", "Patapez", "Brutacio", "Brutilda", "Estoico", "Bocón", "Valka"]

        #Guerreros randoms
        self.randoms_warriors = {"Guerreros de Berk":5, "Guerreras de Berk":5, "Ancianos de Berk":5}

        #Dragones de la franquicia
        self.franquicia_dragons = ["Chimuelo", "Astrid", "Patán", "Patapez", "Brutacio", "Brutilda", "Estoico", "Bocón", "Valka"]

        #Dragones libres
        self.free_dragons = {
            "Terror Terrible": 5,
            "Nadder Mortal": 3,
            "Gronckle": 2,
            "Cremallerus Espantosu": 3,
            "Monstrous Nightmare": 3,
            "Light Fury": 1,
            "Thunderdrum": 1
        }

        #Asignacion de dragones-duenios
        self.dragons_properties = {
            "Night Fury": "Hippo",
            "Nadder Mortal": "Astrid", 
            "Gronckle": "Patapez",
            "Gronckle2": "Bocón",
            "Cremallerus Espantosu": ["Brutacio", "Brutilda"],
            "Monstrous Nightmare": "Patán",
            "Skullcrusher": "Estoico",
            "Stormcutter": "Valka"
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
            "Botas de hierro": 10
        }

        #ovejas
        self.ovejas = 20

        #Registro de participacion diaria
        self.dayli_participation = {}

        def fecha_actual(self):
            return datetime.now().strftime("%Y-%m-%d")

