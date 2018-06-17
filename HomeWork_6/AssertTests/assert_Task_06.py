"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""


def comparison_f(some_list):
    new_list = []
    for i in range(1, len(some_list)):
        if some_list[i] > some_list[i - 1]:
            new_list.append(some_list[i])
    return new_list


if __name__ == '__main__':
    assert comparison_f([1, 2, 3, 4]) == [2, 3, 4]
    assert comparison_f([2, 3, 100, 4]) == [3, 100]
    assert comparison_f([-10, -2, 0, 4]) == [-2, 0, 4]
