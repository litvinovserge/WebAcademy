'''
Написать функцию которая находит факториал числа.
'''

def calc_factorial(n):
    n = int(n)
    if n < 0:
        print('Факториал для отрицательных чисел не вычисляется')
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        i = 0
        while i < n:
            i += 1
            factorial *= i
        return factorial

# начало основной программы
user_number = input('Введите любое число для вычисления факториала: ')
print('Факториал от числа', user_number, 'равеняется =', calc_factorial(user_number ))