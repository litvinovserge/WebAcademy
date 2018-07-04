"""
Перевернуть список
[1, 2, 3, 4] -> [4, 3, 2, 1]
"""

def sort_func(input_list):
    buf = []
    for i in range(len(input_list) - 1, -1, - 1):
        buf.append(input_list[i])
    return buf

if __name__ == '__main__':
    s_data = [1, 2, 3, 4]
    print('Список до замены', s_data)
    print('Список после замены', sort_func(s_data))
