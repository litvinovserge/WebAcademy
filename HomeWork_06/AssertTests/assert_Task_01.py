"""
Найти номер и значение первого положительного элемента
списка.
"""


def positive_list_element_finder(some_list):
    for i in range(len(some_list)):
        if some_list[i] > 0:
            return i, some_list[i]


if __name__ == '__main__':
    assert positive_list_element_finder([-1, 2, 5]) == (1, 2)
    assert positive_list_element_finder([1, 2, 5]) == (0, 1)
    assert positive_list_element_finder([-1, -2, 5]) == (2, 5)
    assert positive_list_element_finder([-1, -2, -5]) is None