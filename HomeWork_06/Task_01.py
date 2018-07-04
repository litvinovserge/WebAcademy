"""
Найти номер и значение первого положительного элемента
списка.
"""
import random
LIST_SIZE = 5


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def positive_list_element_finder(some_list):
    for i in range(len(some_list)):
        if some_list[i] > 0:
            return some_list[i], i
    return 'В списке нет положительных элементов', '-'


if __name__ == '__main__':
    def_list = list_generator(LIST_SIZE)
    print('В случайном списке:', def_list, '\n'
          '1-й положительный элемент равен =', positive_list_element_finder(def_list)[0], '\n'
          'Индекс данного элемента равен =', positive_list_element_finder(def_list)[1]
          )
