"""
Дан некоторый список. Соединить элементы таким образом, чтобы между словами было не более одного пробела.

Исходные данные:
words = ['Lorem', ' ipsum', 'dolor ', 'sit', 'amet,', ' ', 'consectetur', 'adipiscing', 'elit,',
' ', 'sed', 'do', '', 'eiusmod', ' ', ' tempor', 'incididunt', 'ut', ' ' 'labore', ' et ',
'dolore', ' magna', 'aliqua.']


Результат:
''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua.''
"""
words = [
    'Lorem', ' ipsum', 'dolor ', 'sit', 'amet,', ' ', ' consectetur ', 'adipiscing  ', ' elit,', '  ', 'sed', 'do', '',
    'eiusmod', ' ', ' tempor', 'incididunt', 'ut', ' ' 'labore ', ' et  ', 'dolore', ' magna ', 'aliqua.'
]


if __name__ == '__main__':
    output = map(lambda i: i.replace(' ', ''), words)
    output = filter(lambda i: i != '', output)
    print(' '.join(output))
