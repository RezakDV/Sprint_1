world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
# Добавляем в словарь ключ 2022 и его значение 'Аргентина'
world_champions[2022] = 'Аргентина'

# Создаем цикл для вывода ключа и его значения из словаря world_champions
for year, country in world_champions.items():
    print(f'{year} - {country}')

country = 'Италия'

# Проверяем содержит ли словарь world_champions значение, совпадающее с переменной country
if country in world_champions.values():
    print(f'{country} cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print(f'{country} не выигрывала чемпионат мира по футболу в 21 веке.')    