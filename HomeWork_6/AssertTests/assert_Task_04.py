"""
В списке найти минимальный и максимальный элементы,
поменять их местами.
"""


def list_converter(some_list):
    temp_max = some_list[0]
    temp_min = some_list[0]
    index_max = 0
    index_min = 0
    for i in range(len(some_list)):
        if some_list[i] > temp_max:
            temp_max = some_list[i]
            index_max = i
        if some_list[i] < temp_min:
            temp_min = some_list[i]
            index_min = i

    some_list[index_max] = temp_min
    some_list[index_min] = temp_max
    return some_list


if __name__ == '__main__':
    assert list_converter([1, 2, 3]) == [3, 2, 1]
    assert list_converter([1, 1, 1]) == [1, 1, 1]
    assert list_converter([2, 2, 1]) == [1, 2, 2]