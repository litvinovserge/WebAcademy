"""
Сгенерировать список размером 10х10 с помощью функции задания 1
1: Заменить по главной диагонали все числа на 0
2: Заменить все четные числа на 1, не четные на 0
3: Вывести строку таблицы с максимальной суммой элементов
4: Повернуть таблицу на 90 градусов, по часовой, против часовой
"""
import random, copy

def list_generator(list_dimension):
    my_list = [None] * list_dimension
    for i in range(list_dimension):
        my_list[i] = [None] * list_dimension
        for j in range(list_dimension):
            my_list[i][j] = random.randint(100, 999)
    return(my_list)

def list_decorator(some_list):
    for i in range(len(some_list)):
        for j in range(len(some_list[i])):
            if j == 0:
                print('|' + str(some_list[i][j]) + '|', end='')
            else:
                print(str(some_list[i][j]) + '|', end='')
        print()

if __name__ == '__main__':
    user_options = input('Какое действие Вы хотите произвести?' + '\n'
                         '1 - Заменить по главной диагонали матрицы все числа на 0' + '\n'
                         '2 - Заменить все четные числа матрицы на 1, а не четные на 0' + '\n'
                         '3 - Вывести строку таблицы с максимальной суммой элементов' + '\n'
                         '4 - Повернуть таблицу на 90 градусов, по часовой, против часовой' + '\n'
                         '*****************' + '\n'
                         )

    # инициализация случайного массива NxN размерности
    my_list = list_generator(10)
    print('Начальный массив')
    list_decorator(my_list)

    # 1 - Заменить по главной диагонали все числа на 0
    if user_options == '1':
        for i in range(len(my_list)):
            for j in range(len(my_list)):
                if j == i:
                    my_list[j][j] = '000'

        print('По главной диагонали все числа меняем на 0')
        list_decorator(my_list)

    # 2 - Заменить все четные числа на 1, а не четные на 0
    elif user_options == '2':
        for i in range(len(my_list)):
            for j in range(len(my_list)):
                if my_list[i][j] % 2 == 0:
                    my_list[i][j] = 1
                else:
                    my_list[i][j] = 0

        print('Меняем все четные числа на 1, а не четные на 0')
        list_decorator(my_list)

    # 3 - Вывести строку таблицы с максимальной суммой элементов
    elif user_options == '3':
        buf_max = 0
        t_list = []
        for i in range(len(my_list)):
            if sum(my_list[i]) > buf_max:
                buf_max = sum(my_list[i])
                t_list = my_list[i]

        print('Строка с максимальной суммой элементов данного массива:', t_list, sep='\n')

    # 4 - Повернуть таблицу на 90 градусов, по часовой и против часовой стрелки
    elif user_options == '4':
        buf = list_generator(10)

        # 4.1 Поворачиваем таблицу по часовой стрелке
        for i in range(len(my_list)):
            for j in range(len(my_list)):
                buf[i][j] = my_list[j][i]
        print('Поворачиваем таблицу на 90 градусов по часовой стрелке')
        list_decorator(buf)

        # 4.2 Поворачиваем таблицу против часовой стрелки
        for i in range(len(my_list)):
            for j in range(len(my_list)):
                buf[i][j] = my_list[j][len(my_list) - 1 - i]
        print('Поворачиваем таблицу на 90 градусов против часовой стрелки')
        list_decorator(buf)

    # обработка исключений для ввода
    else:
        print('Ошибочный ввод')
