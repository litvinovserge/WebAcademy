"""
Дано два списка значений, вывести значения которые есть в обоих списках.
[1,2,3,4] [3, 5, 7, 1] -> [1, 3]
"""
import random
LIST_SIZE = 5


def list_generator(list_dimension):
    my_list = []
    for i in range(list_dimension):
        my_list.append(random.randint(-9, 9))
    return my_list


def list_comparison(list_1, list_2):
    new_list = []
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                new_list.append(list_1[i])
    return new_list


if __name__ == '__main__':
    list_1 = list_generator(LIST_SIZE)
    list_2 = list_generator(LIST_SIZE)
    print('Для списков:', list_1, 'и :', list_2, '\n'
          'общими значениями являются:', list_comparison(list_1, list_2)
         )