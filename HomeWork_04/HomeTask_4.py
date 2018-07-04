"""
Заменить элементы с нечетными номерами на 0
[1, 1, 1, 1, 1] -> [1, 0, 1, 0, 1]
"""

def mod_func(input_list):
    for i in range(1, len(input_list), 2):
        input_list[i] = 0
    return input_list

if __name__ == '__main__':
    s_data = [1, 2, 3, 4, 5, 6, 7, 8]
    print('Список до замены', s_data)
    print('Список после замены', mod_func(s_data))
