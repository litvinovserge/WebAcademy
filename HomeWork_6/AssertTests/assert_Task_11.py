"""
Дан список значений. Превратить список в словарь где ключами служат элементы списка,
а значениями квадраты этих элементов.
[1,2,3] -> {1:1, 2:4, 3:9}
"""


def dict_2_list(some_list):
    my_dict = {}
    for i in range(len(some_list)):
        my_dict[some_list[i]] = some_list[i] ** 2
    return my_dict


if __name__ == '__main__':
    assert dict_2_list([1, 2, 3]) == {1: 1, 2: 4, 3: 9}