'''
Известны площади круга и квадрата.
Определить:
1. уместится ли круг в квадрате
2. уместится ли квадрат в круге
'''
import math

square_sq = float(input('Введите площадь квадрата: '))
circle_sq = float(input('Введите площадь круга: '))

square_side = square_sq ** 0.5
square_diagonal = square_side * 2 ** 0.5
circle_radius = (circle_sq / math.pi)
circle_diameter = 2 * circle_radius


#проверяем уместится ли круг в квадрате
if square_side >= circle_diameter:
    print('Круг уместится в квадрате')
else:
    print('Круг не уместится в квадрате')

#проверяем уместится ли квадрат в круге
if  circle_diameter >= square_diagonal:
    print('Квадрат уместится в круге')
else:
    print('Квадрат не уместится в круге')





