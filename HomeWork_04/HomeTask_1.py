"""
Дан список чисел, заменить каждый отрицательный элемент на следующий
[1, 2, -3, 5, -6, 7, -9] -> [1, 2, 5, 5, 7, 7, -9]
"""

def neg_func(input_list):
    for i in range(len(input_list) - 1):
        if input_list[i] < 0:
            input_list[i] = input_list[i + 1]
    return input_list

if __name__ == '__main__':
    s_data = [1, 2, -3, 5, -6, 7, -9]
    print('Список до замены', s_data)
    print('Список после замены', neg_func(s_data))
