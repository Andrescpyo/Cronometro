import time
from cronometro import Cronometro

hora = input("Ingrese la hora en formato HH:MM:SS: ")

horas, minutos, segundos = map(int, hora.split(":"))
total_segundos = horas * 3600 + minutos * 60 + segundos + 1

print("La hora ingresada en segundos es:", total_segundos)

c = Cronometro()

for i in range(total_segundos):
    #str.format() <--- se usa para formatear los valores de hora, minuto y segundo.
    hora_actual = "{:02d}".format(c.hora.valor)
    minuto_actual = "{:02d}".format(c.minuto.valor)
    segundo_actual = "{:02d}".format(c.segundo.valor)
    time.sleep(1)
    print(f"{hora_actual}:{minuto_actual}:{segundo_actual}")
    c.avanzar()