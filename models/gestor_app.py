import os
import json
import datetime
from models.creador_de_eventos import Evento
from models.gestor_de_recursos import GestorEventos
from models.validador_de_fechas import verificar_disponibilidad_arena, recomendar_fecha
from models.validador_de_reglas import verificar_participacion_diaria, verificar_dragones_con_su_guerrero, verificacion_del_cremallerus, verificacion_evento_ovejas, verificacion_evento_excursion

class AppManager:

    def __init__(self):
        self.gestor=GestorEventos()
        self.archivo_eventos="eventos.json"
        self.cargar_eventos()

    def cargar_eventos(self):
        try:
            # Primero, crear el archivo si no existe
            if not os.path.exists(self.archivo_eventos):
                with open(self.archivo_eventos, 'w') as f:
                    json.dump([], f)
                self.eventos = []
                return

            with open(self.archivo_eventos, 'r', encoding='utf-8') as f:
                eventos_data = json.load(f)
                self.eventos = []

                for evento_data in eventos_data:
                    # VERIFICAR que los campos existen
                    if not all(key in evento_data for key in ['title', 'type_of_event', 'arena']):
                        continue  # Saltar eventos corruptos
                    
                    evento = Evento(
                        title=evento_data['title'],
                        start_date=datetime.now().date(),  # Fecha por defecto
                        start_time=datetime.now().time(),  # Hora por defecto
                        finish_date=datetime.now().date(),
                        finish_time=datetime.now().time(),
                        type_of_event=evento_data['type_of_event'],
                        arena=evento_data['arena'],
                        warriors=evento_data.get('warriors', []),
                        dragons=evento_data.get('dragons', []),
                        weapons=evento_data.get('weapons', []),
                        armors=evento_data.get('armors', []),
                        extra=evento_data.get('extra')
                    )
                    self.eventos.append(evento)
                
        except Exception as e:
            print(f"Error cargando eventos, comenzando con lista vacía: {e}")
            self.eventos = []


    def guardar_eventos(self):
        eventos_data = []
        for evento in self.eventos:
            eventos_data.append(evento.to_dict())
        
        with open(self.archivo_eventos, 'w', encoding='utf-8') as f:
            json.dump(eventos_data, f, ensure_ascii=False, indent=2)

    
    def crear_evento(self, evento_data):
        """
        Validar y crear un nuevo evento usando tus funciones
        
        evento_data: diccionario con los datos del evento
        """
        # 1. Verificar disponibilidad de arena (usando tu función)
        if not verificar_disponibilidad_arena(
            self.gestor,  # Pasamos el gestor como self
            evento_data['arena'],
            evento_data['start_date'],
            evento_data['start_time'],
            evento_data['finish_date'],
            evento_data['finish_time']
        ):
            return False, "La arena no está disponible en ese horario"
        
        # 2. Verificar participación diaria (Regla 2)
        fecha_str = evento_data['start_date'].strftime("%Y-%m-%d")
        valido, mensaje = verificar_participacion_diaria(
            self.gestor,
            evento_data.get('warriors', []),
            evento_data.get('dragons', []),
            fecha_str
        )
        if not valido:
            return False, mensaje
        
        # 3. Verificar dragones con su guerrero (Regla 3)
        valido, mensaje = verificar_dragones_con_su_guerrero(
            self.gestor,
            evento_data.get('warriors', []),
            evento_data.get('dragons', []),
            evento_data['type_of_event']
        )
        if not valido:
            return False, mensaje
        
        # 4. Verificar Cremallerus (Regla 4)
        valido, mensaje = verificacion_del_cremallerus(
            self.gestor,
            evento_data.get('dragons', []),
            evento_data.get('warriors', []),
            evento_data['type_of_event']
        )
        if not valido:
            return False, mensaje
        
        # 5. Verificar evento de ovejas (Regla 5)
        valido, mensaje = verificacion_evento_ovejas(
            self.gestor,
            evento_data['type_of_event'],
            evento_data['arena'],
            evento_data.get('extra', 0) if evento_data.get('extra') else 0
        )
        if not valido:
            return False, mensaje
        
        # 6. Verificar evento de excursión (Regla 6)
        valido, mensaje = verificacion_evento_excursion(
            self.gestor,
            evento_data['type_of_event'],
            evento_data['arena']
        )
        if not valido:
            return False, mensaje
        
        # 7. Crear el objeto Evento
        evento = Evento(**evento_data)
        
        # 8. Agregar a la lista y guardar
        self.eventos.append(evento)
        self.guardar_eventos()
        
        # 9. Actualizar recursos en el gestor
        self.actualizar_recursos(evento)
        
        return True, "Evento creado exitosamente"
    

    def actualizar_recursos(self, evento):
        """Actualizar recursos después de crear evento"""
       #falta el actualizador de recursos, x ahora solo hay de fechas de participacion

        fecha_str = evento.start_date.strftime("%Y-%m-%d")
        if fecha_str not in self.gestor.daily_participation:
            self.gestor.daily_participation[fecha_str] = {"guerreros": set(), "dragones": set()}
        
        self.gestor.daily_participation[fecha_str]["guerreros"].update(evento.warriors)
        self.gestor.daily_participation[fecha_str]["dragones"].update(evento.dragons)

    
    def obtener_eventos_futuros(self):
        """Obtener eventos futuros"""
        ahora = datetime.now()
        eventos_futuros = []
        
        for evento in self.eventos:
            # Crear datetime combinando fecha y hora
            inicio = datetime.combine(evento.start_date, evento.start_time)
            if inicio > ahora:
                eventos_futuros.append(evento)
        
        return eventos_futuros
    

    def eliminar_evento(self, index):
        """Eliminar evento por índice"""
        if 0 <= index < len(self.eventos):
            evento_eliminado = self.eventos.pop(index)
            self.guardar_eventos()
            
            # Liberar recursos (participación diaria)
            fecha_str = evento_eliminado.start_date.strftime("%Y-%m-%d")
            if fecha_str in self.gestor.daily_participation:
                for guerrero in evento_eliminado.warriors:
                    self.gestor.daily_participation[fecha_str]["guerreros"].discard(guerrero)
                for dragon in evento_eliminado.dragons:
                    self.gestor.daily_participation[fecha_str]["dragones"].discard(dragon)
            
            return True, "Evento eliminado"
        return False, "Índice inválido"
