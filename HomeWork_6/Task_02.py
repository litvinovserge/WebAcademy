"""
Найти сумму положительных элементов списка.
"""
import random
LIST_SIZE = 5


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def sum_of_positives(some_list):
    my_sum = 0
    for i in range(len(some_list)):
        if some_list[i] > 0:
            my_sum += some_list[i]
    return my_sum


if __name__ == '__main__':
    def_list = list_generator(LIST_SIZE)
    print('Сумма всех положительных элементов списка:', def_list, '\n'
          'равняется =', sum_of_positives(def_list)
          )
