"""
Дан список значений. Превратить список в словарь поочередно превращая елементы в ключи и значения.
[1, 2, 3, 4, 5, 6] -> {1: 2, 3: 4, 5: 6}
"""
import random
LIST_SIZE = 10


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def list_2_dict(some_list):
    my_dict = {}
    for i in range(len(some_list) - 1):
        if i % 2 == 0:
            if some_list[i] in my_dict.keys():
                some_list[i] = str(some_list[i]) + '_duplicate'
                my_dict[some_list[i]] = some_list[i + 1]
            else:
                my_dict[some_list[i]] = some_list[i + 1]
    return my_dict


if __name__ == '__main__':
    new_list = list_generator(LIST_SIZE)
    print('Превращаем список:', new_list)
    print('В словарь:', list_2_dict(new_list))

