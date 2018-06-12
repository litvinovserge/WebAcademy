"""
Заменить каждый элемент на следующий, последний на первый
[1, 2, 3, 4] -> [4, 1, 2, 3]
"""

def sort_func(input_list):
    buf = list(input_list)
    input_list[0] = input_list[-1]
    for i in range(len(input_list) - 1):
        input_list[i + 1] = buf[i]
    return input_list

if __name__ == '__main__':
    s_data = [1, 2, 3, 4]
    print('Список до замены', s_data)
    print('Список после замены', sort_func(s_data))
