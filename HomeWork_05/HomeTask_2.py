"""
Написать функцию, которая выводит двухмерный список в виде таблицы
Пример
>>print_list([[222, 113], [456, 500]])
—————
| 222 | 113 |
—————
| 456 | 500 |
—————
"""

def list_decorator(some_list):
    for i in range(len(some_list)):
        print('-' * (2 * len(some_list[i]) + 1))
        for j in range(len(some_list[i])):
            if j == 0:
                print('|' + str(some_list[i][j]) + '|', end='')
            else:
                print(str(some_list[i][j]) + '|', end='')
        print()
    print('-' * (2 * len(some_list[i]) + 1))

if __name__ == '__main__':
    test_list = [
        [1, 2, 2, 4, 3],
        [3, 4, 2, 4, 1],
        [3, 5, 8, 3, 0]
         ]
    list_decorator(test_list)