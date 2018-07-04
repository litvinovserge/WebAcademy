"""
Дан список значений. Превратить список в словарь поочередно превращая елементы в ключи и значения.
[1, 2, 3, 4, 5, 6] -> {1: 2, 3: 4, 5: 6}
"""


def list_2_dict(some_list):
    my_dict = {}
    for i in range(len(some_list) - 1):
        if i % 2 == 0:
            my_dict[some_list[i]] = some_list[i + 1]
    return my_dict


if __name__ == '__main__':
    assert list_2_dict([1, 2, 3, 4, 5]) == {1: 2, 3: 4}
    assert list_2_dict(['k', 'v', 'k2', 'v2']) == {'k': 'v', 'k2': 'v2'}