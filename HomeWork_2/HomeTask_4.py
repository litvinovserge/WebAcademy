'''
Вывести на экран фигуры из звездочек:
Ромб, Елочка, Треугольник, Квадрат, ступеньки
'''
PICT_SYMBOL = '*'

print('выводим ромб')
rhomb_length = 7
for i in range(1, rhomb_length + 1):
    if i % 2 != 0:
        space_length = (rhomb_length - i) // 2
        print(' ' * space_length + PICT_SYMBOL * i)
for i in range(rhomb_length - 1, 0, -1):
    if i % 2 != 0:
        space_length = (rhomb_length - i) // 2
        print(' ' * space_length + PICT_SYMBOL * i)

print('выводим ёлочку')
tree_side = 10
for i in range(1, tree_side + 1):
    if i % 2 != 0:
        space_length = (tree_side - i) // 2
        print(' ' * space_length + PICT_SYMBOL * i  + ' ' * space_length)

print('выводим треугольник')
triangle_side = 10
for i in range(1, triangle_side + 1):
    print(PICT_SYMBOL * i)

print('выводим квадрат')
square_side = 7
for i in range(1, square_side + 1):
    print(PICT_SYMBOL * square_side)

print('выводим ступеньки')
stairs_height = 10
for i in range(1, stairs_height + 1):
    space_length = stairs_height - i
    print(' ' * space_length + PICT_SYMBOL * i)



