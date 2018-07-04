"""
Дан список, содержащий положительные и отрицательные
числа. Заменить все элементы списка на противоположные по
знаку. Например, задан список [1, -5, 0, 3, -4]. После
преобразования должно получиться [-1, 5, 0, -3, 4].
"""


def list_converter(some_list):
    for i in range(len(some_list)):
        some_list[i] = -some_list[i]
    return some_list


if __name__ == '__main__':
    assert list_converter([-1, -2, -3]) == [1, 2, 3]
    assert list_converter([1, 1, 1]) == [-1, -1, -1]
    assert list_converter([]) == []
    assert list_converter([1, -1, 0]) == [-1, 1, 0]