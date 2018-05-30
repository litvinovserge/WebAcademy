"""
Задача №2
Вычислить возраст человека. Программа принимает с клавиатуры год рождения и выводит возраст на экран.
"""
#подгрузка модуля для работы с датой
import datetime

birth_date = int(input ('Введите Ваш год рождения: '))
current_year = int(datetime.datetime.today().year)

print ('Ваш текущий возраст: ',current_year - birth_date,' лет')

