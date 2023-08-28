import time
import os
from cronometro import Cronometro

hora = input("\nIngrese la hora en formato HH:MM:SS: ")

horas, minutos, segundos = map(int, hora.split(":"))
total_segundos = horas * 3600 + minutos * 60 + segundos + 1

c = Cronometro()

for i in range(total_segundos):
    #str.format() <--- se usa para formatear los valores de hora, minuto y segundo.
    hora_actual = "{:02d}".format(c.hora.valor)
    minuto_actual = "{:02d}".format(c.minuto.valor)
    segundo_actual = "{:02d}".format(c.segundo.valor)

    cronometro_str = f"\r{hora_actual} : {minuto_actual} : {segundo_actual}"
    print("\n", cronometro_str, end="")

    # Hacemos que los dos puntos parpadeen
    if i % 2 == 0:  
        cronometro_str = f"\r{hora_actual}   {minuto_actual}   {segundo_actual}"
    print(cronometro_str, end="")

    c.avanzar()
    time.sleep(1)

    #os.system  hace que la siguiente impresión sobrescriba la línea anterior.
    os.system('cls' if os.name == "nt" else  'clear')
    
print("\n¡Tiempo terminado! :3\n")