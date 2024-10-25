from datetime import timedelta

distancia_metros = 65 * 1000  ## 65 km em metros ##

horas = 3
minutos = 23
segundos = 17

tempo_total = timedelta(hours=horas, minutes=minutos, seconds=segundos)

tempo_total_segundos = tempo_total.total_seconds()

velocidade_media = distancia_metros / tempo_total_segundos

print(velocidade_media)
