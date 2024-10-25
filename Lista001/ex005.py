from datetime import timedelta

horas = 2
minutos = 30
segundos = 45

tempo = timedelta(hours=horas, minutes=minutos, seconds=segundos)

total_segundos = tempo.total_seconds()

print(total_segundos)