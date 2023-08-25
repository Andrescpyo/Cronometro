from cronometro import Cronometro

hora = input("Ingrese la hora en formato HH:MM:SS: ")

horas, minutos, segundos = map(int, hora.split(":"))
total_segundos = horas * 3600 + minutos * 60 + segundos + 1

print("La hora ingresada en segundos es:", total_segundos)

c = Cronometro()

for i in range (total_segundos):
    print(c.hora.valor, ":", c.minuto.valor, ":", c.segundo.valor)
    c.avanzar()