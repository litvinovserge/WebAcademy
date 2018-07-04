"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
import random
LIST_SIZE = 10


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def comparison_f(some_list):
    new_list = []
    for i in range(1, len(some_list)):
        if some_list[i] > some_list[i - 1]:
            new_list.append(some_list[i])
    return new_list


if __name__ == '__main__':
    def_list = list_generator(LIST_SIZE)
    print('Для списка:', def_list, '\n'
          'Выводим элементы, которые больше предыдущего элемента:', comparison_f(def_list)
          )
