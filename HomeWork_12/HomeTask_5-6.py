"""
Создать клас Person c атрибутами name и age. Создать список с некоторым количеством экземпляров класса Person.
Можно использовать генератор с прошлой дз.

1. Отсоритровать список людей по возрасту.
до: [Person('elias', 23), Person('Bob', 11), Person('Kevin', 46)]
после: [Person('Bob', 11), Person('elias', 23), Person('Kevin', 46)]

2. Найти самого старшего человека.
3. Найти самого младшего человека.

list(map(lambda x: str(x), group_of_people))
"""
import random

NAMES = 'names.txt'
AGE_LIMITS = [18, 80]


class Person:

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
        if not any((name, age)):
            self.name, self.age = next(self.person_generator())

    def __str__(self):
        return f'{self.name}: {self.age}yo'

    @staticmethod
    def person_generator(name=None, age=None):
        if not name:
            with open(NAMES, 'r') as file:
                name = random.choice([each.strip() for each in file.read().split(',')])
        if not age:
            age = random.randint(AGE_LIMITS[0], AGE_LIMITS[1])
        yield [name, age]


def str_representation(some_class):
    """
    :param some_class: принимаем экземляр/экземпляры любого класса
    :return: список с элементами в строковом представлением класса
    """
    return list(map(lambda x: str(x), some_class))


if __name__ == '__main__':
    group_of_people = [Person() for i in range(10)]
    xxx = sorted(group_of_people, key=lambda each: each.age)
    print(
        f'Начальная группа людей: {str_representation(group_of_people)}',
        f'Сортируем группу по возрасту:, {str_representation(sorted(group_of_people, key=lambda each: each.age))}',
        f'Находим самого старшего: {max(group_of_people, key=lambda each: each.age)}',
        f'Находим самого старшего: {min(group_of_people, key=lambda each: each.age)}',
        sep='\n'
    )