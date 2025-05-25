# Инициализируем строку с временными интервалами
time_string = '1h 45m,360s,25m,30m 120s,2h 60s' 

# Разбиваем строку на отдельные временные интервалы по запятой
time_string = time_string.split(',')

# Инициализируем переменную для хранения общего количества минут
total_minutes = 0

# Разбиваем каждый временной интервал по пробелу
for time in time_string:
    time_units = time.split(' ')

# Обрабатываем каждый временной интервал
    for unit in time_units:
        if 'h' in unit:
            total_minutes += int(unit.replace('h', '')) * 60
        elif 'm' in unit:
            total_minutes += int(unit.replace('m', ''))
        elif 's' in unit:
            total_minutes += int(unit.replace('s', '')) // 60

print(total_minutes)

