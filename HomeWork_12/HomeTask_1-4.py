"""
1 - Дана строка чисел, получить такую же строку с отсортированными числами.
до: '1,34,2,6,18,19'
после: '1,2,6,18,19,34'

2 - Дан список строк. Отфильтровать все пустые строки.
до: ['hello', '', 'world', '', '', '', '!!']
после: ['hello', 'world', '!!']

3 - Дан список словарей. Отфильтровать все элементы где value = 0.
до: [{'id': 1, 'value': 0}, {'id': 2, 'value': 256}, {'id': 4, 'value': 0}, {'id': 10, 'value': 1024}]
после: [{'id': 2, 'value': 256}, {'id': 10, 'value': 1024}]

4 - Дан список положительных и отрицательных значений отсортировать элементы по модулю.
(Модуль абсолютное значение числа abs(-5) = 5 a abs(5) = 5).
до: [-10, 12, 6, -4, -2, 8]
после: [-2, -4, 6, 8, -10, 12]
"""


if __name__ == '__main__':

    # 1
    some_string = '1,34,2,6,18,19'
    print('Task 1:', ','.join(sorted(some_string.split(','), key=int)))

    # 2
    values = ['hello', '', 'world', '', '', '', '!!']
    print('Task 2:', *filter(lambda x: x != '', values))

    # 3
    values = [{'id': 1, 'value': 0}, {'id': 2, 'value': 256}, {'id': 4, 'value': 0}, {'id': 10, 'value': 1024}]
    print('Task 3:', *filter(lambda x: x['value'] != 0, values))

    # 4
    values = [-10, 12, 6, -4, -2, 8]
    print('Task 4:', sorted(values, key=lambda x: abs(x)))

