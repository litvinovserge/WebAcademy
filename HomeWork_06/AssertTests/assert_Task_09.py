"""
Из одномерного списка удалить все повторяющиеся элементы (дубликаты) так, чтобы каждое значение встречалось в списке
только один раз.
"""


def list_modifier(some_list):
    new_list = []
    for i in range(len(some_list)):
        for j in range(i):
            if some_list[j] == some_list[i]:
                some_list[j] = None
    for i in range(len(some_list)):
        if some_list[i] == 0 or some_list[i]:
            new_list.append(some_list[i])
    return new_list

if __name__ == '__main__':
    assert list_modifier([1, 1, 2]) == [1, 2]