"""
Найти сумму положительных элементов списка.
"""


def sum_of_positives(some_list):
    my_sum = 0
    for i in range(len(some_list)):
        if some_list[i] > 0:
            my_sum += some_list[i]
    return my_sum


if __name__ == '__main__':
    assert sum_of_positives([1, 2, -4, 0]) == 3
    assert sum_of_positives([-1, -2, -3]) == 0
    assert sum_of_positives([1, 1, 1]) == 3
