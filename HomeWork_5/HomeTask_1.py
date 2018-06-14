"""
Написать функцию, которая генерирует список списков (двух мерный массив) размерности NxN заполненный
случайными числами от 100 до 999 (использовать функцию random.randint(100, 999)
ПРИМЕР
>>gen_list(2)
[[222, 113], [456, 500]]
"""
import random

def list_generator(list_dimension):
    my_list = [[None] * list_dimension] * list_dimension
    for i in range(list_dimension):
        for j in range(list_dimension):
            my_list[i][j] = random.randint(100, 999)
    return my_list

if __name__ == '__main__':
    list_dimension = int(input('Задайте размерность для списка списков: '))
    print(list_generator(list_dimension))
