"""
Дано два списка значений, вывести значения которые есть в обоих списках.
[1,2,3,4] [3, 5, 7, 1] -> [1, 3]
"""


def list_comparison(list_1, list_2):
    new_list = []
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                new_list.append(list_1[i])
    return new_list


if __name__ == '__main__':
    assert list_comparison([1, 2, 3], [3, 5, 4]) == [3]
    assert list_comparison([1, 2], [2, 1]) == [1, 2]