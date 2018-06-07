'''
Написать функцию принимающую имя фигуры (квадрат, треугольник, ромб), ее размерность и рисует эту фигуру на экран.
'''
PICT_SYMBOL = '*'

def graph_builder(request):
    if request == 'квадрат':
        square_side = 7
        for i in range(1, square_side + 1):
            print(PICT_SYMBOL * square_side)
    elif request == 'треугольник':
        triangle_side = 10
        for i in range(1, triangle_side + 1):
            if i % 2 != 0:
                space_length = (triangle_side - i) // 2
                print(' ' * space_length + PICT_SYMBOL * i + ' ' * space_length)
    elif request == 'ромб':
        rhomb_length = 7
        for i in range(1, rhomb_length + 1):
            if i % 2 != 0:
                space_length = (rhomb_length - i) // 2
                print(' ' * space_length + PICT_SYMBOL * i)
        for i in range(rhomb_length - 1, 0, -1):
            if i % 2 != 0:
                space_length = (rhomb_length - i) // 2
                print(' ' * space_length + PICT_SYMBOL * i)
    else:
        print('ошибочный ввод, повторите запрос')

# начало основной программы
user_input = input('Введите имя фигуры для отрисовки (квадрат, треугольник, ромб): ')
graph_builder(user_input)