'''
Написать функцию, которая определяет количество разрядов введенного целого числа.
'''

def number_analysis(tens):
    tens = abs(int(tens))
    counter = 1
    if tens == 0:
        return 'ошибочный ввод'
    else:
        while tens > 10:
            tens = tens / 10
            counter += 1
        return counter

# начало основной программы
user_data = input('Введите любое число: ')
print('Количество разрядов данного числа равно:', number_analysis(user_data))