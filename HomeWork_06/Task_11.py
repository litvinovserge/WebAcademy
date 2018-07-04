"""
Дан список значений. Превратить список в словарь где ключами служат элементы списка,
а значениями квадраты этих элементов.
[1,2,3] -> {1:1, 2:4, 3:9}
"""
import random
LIST_SIZE = 5


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def dict_2_list(some_list):
    my_dict = {}
    for i in range(len(some_list)):
        my_dict[some_list[i]] = some_list[i] ** 2
    return my_dict


if __name__ == '__main__':
    some_list = list_generator(LIST_SIZE)
    print('Превращаем список:', some_list, '\n',
          'в словарь:', dict_2_list(some_list))

