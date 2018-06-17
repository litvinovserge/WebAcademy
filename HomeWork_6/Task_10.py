"""
В одномерном списке удалить все четные элементы и оставить только нечетные.
"""
import random
LIST_SIZE = 10


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def list_modifier(some_list):
    new_list = []
    for i in range(len(some_list)):
        if some_list[i] % 2 == 0:
            some_list[i] = None
    for i in range(len(some_list)):
        if some_list[i] == 0 or some_list[i]:
            new_list.append(some_list[i])
    return new_list


if __name__ == '__main__':
    new_list = list_generator(LIST_SIZE)
    print('У списка:', new_list)
    print('Удаляем все четные элементы:', list_modifier(new_list))