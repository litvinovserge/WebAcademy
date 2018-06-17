"""
Дан список чисел.
Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""
import random
LIST_SIZE = 10


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def list_analyser(some_list):
    counter = 0
    for i in range(1, len(some_list) - 1):
        if some_list[i] > some_list[i + 1] and some_list[i] > some_list[i - 1]:
            counter += 1
    return counter


if __name__ == '__main__':
    new_list = list_generator(LIST_SIZE)
    print('Для списка:', new_list,
          'кол-во элементов, которые больше двух своих соседей, равно =', list_analyser(new_list)
          )

