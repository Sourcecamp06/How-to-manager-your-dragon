from datetime import datetime, timedelta

#Verificacion de si la arena esta disponible en la fecha y hora especificadas
def verificar_disponibilidad_arena(self, arena, new_start_date, new_start_time, new_finish_date, new_finish_time):
    for evento in self.eventos:
        if evento.arena == arena and evento.start_date == new_start_date:

            inicio_existente = datetime.strptime(f"{evento.start_date} {evento.start_time}", "%Y-%m-%d %H:%M")
            fin_existente = datetime.strptime(f"{evento.finish_date} {evento.finish_time}", "%Y-%m-%d %H:%M") - inicio_existente
            
            inicio_nuevo = datetime.strptime(f"{new_start_date} {new_start_time}", "%Y-%m-%d %H:%M")
            fin_nuevo = datetime.strptime(f"{new_finish_date} {new_finish_time}", "%Y-%m-%d %H:%M") - inicio_nuevo 
            
            if ((inicio_nuevo >= inicio_existente and inicio_nuevo <= fin_existente) or (fin_nuevo >= inicio_existente and fin_nuevo <= fin_existente) or (inicio_nuevo <= inicio_existente and fin_nuevo >= fin_existente)):
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
def recomendar_fecha(gestor, arena, start_date:datetime, start_time:datetime, finish_date:datetime, finish_time:datetime):
    actual_duration = duration(start_date, start_time, finish_date, finish_time)
    events_list=[]
    for evento in gestor.eventos:
        if arena == evento.arena:
            events_list.append(evento)
    for i in range(len(events_list)):
        for j in range(i, len(events_list)):
            if events_list[i].start_date > events_list[j].start_date:
                events_list[i], events_list[j] = events_list[j], events_list[i]
    actual_inicio= datetime.combine(start_date, start_time) 

    for i in range(1, len(events_list)):
        nuevo_inicio = datetime.combine(events_list[i].start_date, events_list[i].start_time)
        if duration(events_list[i-1].finish_date, events_list[i-1].finish_time, events_list[i].start_date, events_list[i].start_time) >= actual_duration and  nuevo_inicio >= actual_inicio:
            return f"Fecha recomendada: {events_list[i-1].finish_date} a las {events_list[i-1].finish_time}"
    else: 
        return f"Fecha recomendada: {events_list[len(events_list)-1].finish_date} a las {events_list[len(events_list)-1].finish_time}"
