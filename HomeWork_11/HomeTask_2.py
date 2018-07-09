"""
Написать функцию-генератор gmap принимающую два аргумента: функцию и последовательность и применяет в функцию
к каждому элементу последовательности.
Пример:
>>values = [‘1’, ‘3’, ’45’, ’56’]
>>for i in gmap(int, values):
	print(i)
1
3
45
56
"""


def gmap(user_func, user_data):
    for each in list(map(user_func, user_data)):
        yield(each)


if __name__ == '__main__':
    values = ['2', '4', '5', '6']
    for i in gmap(float, values):
        print(i)
