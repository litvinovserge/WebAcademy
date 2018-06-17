"""
В списке найти минимальный и максимальный элементы,
поменять их местами.
"""
import random
LIST_SIZE = 10


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def list_converter(some_list):
    temp_max = 0
    temp_min = 0
    for i in range(len(some_list)):
        if some_list[i] > temp_max:
            temp_max = some_list[i]
            index_max = i
        elif some_list[i] < temp_min:
            temp_min = some_list[i]
            index_min = i

    some_list[index_max] = temp_min
    some_list[index_min] = temp_max
    return some_list


if __name__ == '__main__':
    def_list = list_generator(LIST_SIZE)
    print('Список до преобразований:', def_list)
    print('Список после преобразова:', list_converter(def_list))


