from datetime import datetime, timedelta

#Verificacion de si la arena esta disponible en la fecha y hora especificadas
def verificar_disponibilidad_arena(self, arena, new_date, new_time, new_duration):
    for evento in self.eventos:
        if evento.arena == arena and evento.start_date == new_date:

            inicio_existente = datetime.strptime(f"{new_date} {evento.start_time}", "%Y-%m-%d %H:%M")
            fin_existente = inicio_existente + timedelta(minutes=evento.duration)  
            
            inicio_nuevo = datetime.strptime(f"{new_date} {new_time}", "%Y-%m-%d %H:%M")
            fin_nuevo = inicio_nuevo + timedelta(minutes=new_duration)  
            
            if ((inicio_nuevo > inicio_existente and inicio_nuevo < fin_existente) or (fin_nuevo > inicio_existente and fin_nuevo < fin_existente)):
                return False
            
    return True