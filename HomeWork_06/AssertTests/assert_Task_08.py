"""
Дан список чисел.
Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов.
Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
"""


def list_analyser(some_list):
    counter = 0
    for i in range(1, len(some_list) - 1):
        if some_list[i] > some_list[i + 1] and some_list[i] > some_list[i - 1]:
            counter += 1
    return counter


if __name__ == '__main__':
    assert list_analyser([1, 2, 1, 3, 2]) == 2
    assert list_analyser([1, 2, 3]) == 0
    assert list_analyser([1]) == 0