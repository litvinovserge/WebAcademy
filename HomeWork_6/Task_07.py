"""
Дан список чисел.
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""
import random
LIST_SIZE = 5


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def list_analyser(some_list):
    for i in range(len(some_list) - 1):
        if (some_list[i] < 0 and some_list[i + 1] < 0) or (some_list[i] >= 0 and some_list[i + 1] >= 0):
            return [some_list[i], some_list[i + 1]]
    return 'такой пары нет'


if __name__ == '__main__':
    new_list = list_generator(LIST_SIZE)
    print('Для списка:', new_list, 'пара соседних элементов одного знака: ', list_analyser(new_list))