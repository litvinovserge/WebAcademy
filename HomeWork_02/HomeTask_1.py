'''
Составить программу, которая требует ввести два числа.
Если первое число больше второго, то программа печатает слово больше.
Если первое число меньше второго, то программа печатает слово меньше.
А если числа равны, программа напечатает сообщение Эти числа равны.
'''

n1 = int(input('Введите значение для 1го числа: '))
n2 = int(input('Введите значение для 2го числа: '))

if n1 > n2:
    print('Больше')
elif n1 < n2:
    print('Меньше')
else:
    print('Равны')
