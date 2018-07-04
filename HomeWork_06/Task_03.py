"""
Дан список, содержащий положительные и отрицательные
числа. Заменить все элементы списка на противоположные по
знаку. Например, задан список [1, -5, 0, 3, -4]. После
преобразования должно получиться [-1, 5, 0, -3, 4].
"""
import random
LIST_SIZE = 5


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def list_converter(some_list):
    for i in range(len(some_list)):
        some_list[i] = -some_list[i]
    return some_list


if __name__ == '__main__':
    def_list = list_generator(LIST_SIZE)
    print('Для случайного списка:', def_list)
    print('Наше преобразование выглядит следующим образом:', list_converter(def_list))

