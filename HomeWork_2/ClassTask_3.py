'''
Определить является ли число a делителем числа b
'''

a = float(input('Введите значение для числа a: '))
b = float(input('Введите значение для числа b: '))

if (b % a) == 0:
    print('Число a является делителем числа b')
else:
    print('Число a не является делителем числа b')