"""
Задача №1
Запрограммировать следующее выражение:
(a + b - f / a) + f * a * a - (a + b)
Числа а, b, f вводятся с клавиатуры.
Организовать пользовательский интерфейс, таким образом, чтобы было понятно, в каком порядке должны вводиться числа.
"""

a = float(input('Введите значение для а: '))
b = float(input('Введите значение для b: '))
f = float(input('Введите значение для f: '))

result = (a + b - f  / a) + f * a * a - (a + b)

print ("Результат вычисления выражения (a + b - f / a) + f * a * a - (a + b) равен: ",result)