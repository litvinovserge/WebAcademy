"""
Найти сумму и произведение элементов одномерного числового списка.
"""


def calc_sum(some_list):
    summ = 0
    for i in range(len(some_list)):
        summ += some_list[i]
    return summ


def calc_multp(some_list):
    multp = 1
    for i in range(len(some_list)):
        multp *= some_list[i]
    return multp


if __name__ == '__main__':
    assert calc_sum([1, 2]) == 3
    assert calc_sum([0, -3]) == -3

    assert calc_multp([1, 1]) == 1
    assert calc_multp([2, 3]) == 6
    assert calc_multp([0, 1]) == 0
