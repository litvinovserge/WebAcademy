"""
Дан список чисел.
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""


def list_analyser(some_list):
    new_list = []
    for i in range(len(some_list) - 1):
        if (some_list[i] < 0 and some_list[i + 1] < 0) or (some_list[i] >= 0 and some_list[i + 1] >= 0):
            return some_list[i], some_list[i + 1]
    return []


if __name__ == '__main__':
    assert list_analyser([1, 2, -1, -1]) == (1, 2)
    assert list_analyser([1, 2, 3, 4]) == (1, 2)
    assert list_analyser([1, -1, 2, -4]) == []