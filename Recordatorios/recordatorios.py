from datetime import datetime

def key_func(evento):
    return (datetime.strptime(evento[0], '%Y-%m-%d'), datetime.strptime(evento[1], '%H:%M'))

recordatorios = [['2021-01-01', '11:00', 'Levantarse y ejercitar'],
                 ['2021-05-01', '15:00', 'No trabajar'],
                 ['2021-07-15', '13:00', 'No hacer nada es feriado'],
                 ['2021-09-18', '16:00', 'Ramadas'],
                 ['2021-12-25', '00:00', 'Navidad']]

# 1. Agrega un evento el 2 de Enero de 2021 a las 6 de la mañana para "Empezar el Año".
nuevo_evento_1 = ['2021-01-02', '06:00', 'Empezar el año']
recordatorios.append(nuevo_evento_1)

# 2. Corrige el evento del 15 de Julio para que sea el 16 de Julio.
for evento in recordatorios:
    if 'No hacer nada es feriado' in evento[2]:
        evento[0] = '2021-07-16'

# 3. Elimina el evento del día del trabajo.
recordatorios = [evento for evento in recordatorios if 'No trabajar' not in evento[2]]

# 4. Agrega una cena de Navidad y de Año Nuevo a las 22 hrs.
nuevo_evento_2 = ['2021-12-24', '22:00', 'Cena de Navidad']
nuevo_evento_3 = ['2021-12-31', '22:00', 'Cena de Año Nuevo']
recordatorios.append(nuevo_evento_2)
recordatorios.append(nuevo_evento_3)

# Ordena la lista de recordatorios por fecha y hora
recordatorios.sort(key=key_func)

# Imprime cada evento con un salto de línea
for evento in recordatorios:
    print(evento)
