"""
Найти сумму и произведение элементов одномерного числового списка.
"""
import random
LIST_SIZE = 5


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def calc_list(some_list):
    summ = 0
    multp = 1
    for i in range(len(some_list)):
        summ += some_list[i]
        multp *= some_list[i]
    return summ, multp


if __name__ == '__main__':
    def_list = list_generator(LIST_SIZE)
    print('Для списка', def_list, '\n'
          'Сумма элементов равна =', calc_list(def_list)[0], '\n'
          'Произведение элементов равно =', calc_list(def_list)[1]
          )
