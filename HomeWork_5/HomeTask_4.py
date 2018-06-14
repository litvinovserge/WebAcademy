"""
Отсортировать список методом пузырьковой сортировки.
"""

def sort_b_func(input_list):

    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i):
            if input_list[j] > input_list[j + 1]:
                buf = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = buf
    return input_list

if __name__ == '__main__':
    s_data = [4, 1, 5, 3, 6]
    print('Список до сортировки', s_data)
    print('Список после сортировки', sort_b_func(s_data))
