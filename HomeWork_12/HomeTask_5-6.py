"""
Создать клас Person c атрибутами name и age. Создать список с некоторым количеством экземпляров класса Person.
Можно использовать генератор с прошлой дз.

1. Отсоритровать список людей по возрасту.
до: [Person('elias', 23), Person('Bob', 11), Person('Kevin', 46)]
после: [Person('Bob', 11), Person('elias', 23), Person('Kevin', 46)]

2. Найти самого старшего человека.
3. Найти самого младшего человека.
"""
import random

NAMES = 'names.txt'
AGE_LIMITS = [18, 80]


class Person(list):

    def __init__(self, name=None, age=None):
        super(Person, self).__init__([name, age])
        if not any((name, age)):
            self[0], self[1] = next(self.person_generator(name, age))

    @staticmethod
    def person_generator(name=None, age=None):
        if not name:
            with open(NAMES, 'r') as file:
                name = random.choice([each.strip() for each in file.read().split(',')])
        if not age:
            age = random.randint(AGE_LIMITS[0], AGE_LIMITS[1])
        yield [name, age]


if __name__ == '__main__':
    group_of_people = []
    for i in range(10):
        group_of_people.append(Person())
    print(
        f'Начальная группа людей:, {group_of_people}',
        f'Сортируем группу по возрасту:, {sorted(group_of_people, key=lambda each: each[1])}',
        f'Находим самого старшего: {max(group_of_people, key=lambda each: each[1])}',
        f'Находим самого старшего: {min(group_of_people, key=lambda each: each[1])}',
        sep='\n'
    )