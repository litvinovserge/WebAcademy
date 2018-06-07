'''
Написать аналог функции len
'''

def my_len(any_data):
    counter = 0
    for i in any_data:
        counter += 1
    return counter

user_data = ('Введите данные: ')
print('Длина ваших данных равна =', my_len(user_data))
