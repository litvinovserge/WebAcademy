"""
В одномерном списке удалить все четные элементы и оставить только нечетные.
"""


def list_modifier(some_list):
    new_list = []
    for i in range(len(some_list)):
        if some_list[i] % 2 == 0:
            some_list[i] = None
    for i in range(len(some_list)):
        if some_list[i] == 0 or some_list[i]:
            new_list.append(some_list[i])
    return new_list


if __name__ == '__main__':
    assert list_modifier([1, 2, 3, 4]) == [1, 3]
    assert list_modifier([0, 1, 1]) == [1, 1]