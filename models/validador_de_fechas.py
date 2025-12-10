from datetime import datetime, timedelta, strptime 

#Verificacion de si la arena esta disponible en la fecha y hora especificadas
def verificar_disponibilidad_arena(self, arena, new_start_date, new_start_time, new_finish_date, new_finish_time):
    for evento in self.eventos:
        if evento.arena == arena and evento.start_date == new_start_date:

            inicio_existente = strptime(f"{evento.start_date} {evento.start_time}", "%Y-%m-%d %H:%M")
            fin_existente = strptime(f"{evento.finish_date} {evento.finish_time}", "%Y-%m-%d %H:%M") - inicio_existente
            
            inicio_nuevo = strptime(f"{new_start_date} {new_start_time}", "%Y-%m-%d %H:%M")
            fin_nuevo = strptime(f"{new_finish_date} {new_finish_time}", "%Y-%m-%d %H:%M") - inicio_nuevo 
            
            if ((inicio_nuevo >= inicio_existente and inicio_nuevo <= fin_existente) or (fin_nuevo >= inicio_existente and fin_nuevo <= fin_existente) or (inicio_nuevo <= inicio_existente and fin_nuevo >= fin_existente)):
                return False
            
    return True

#Duracion de eventos
def duration(self, start_date:datetime, start_time:datetime, finish_date:datetime, finish_time:datetime):
    start = datetime.combine(start_date, start_time)
    finish = datetime.combine(finish_date, finish_time)
    duration = abs(finish - start)
    duration = duration.total_seconds()/60
    return duration

#Buscar hueco
def recomendar_fecha(self):
    actual_duration = self.duration(self.start_date, self.start_time, self.finish_date, self.finish_time)
    durations = []
    for i in range(len(self.eventos)-1):
        durations.append(self.duration(self.eventos[i+1].start_date, self.eventos[i+1].start_time, self.eventos[i].finish_date, self.eventos[i].finish_time))
