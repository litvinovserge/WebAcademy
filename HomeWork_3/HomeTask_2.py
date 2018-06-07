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
        for i in range(2, n+1):
            factorial = (n - 1) * n
        return factorial

# начало основной программы
user_number = input('Введите любое число для вычисления факториала: ')
print('Факториал от числа', user_number, 'равеняется =', calc_factorial(user_number ))