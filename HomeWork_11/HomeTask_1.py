"""
1. Написать функцию-генератор генерирующую данные о людях.
Пример:
>>for person in gen_person():
	print(person)
[‘Alex’, ‘Smith’, 23]
[‘Bob’ , ‘Alan’, 44]

2. Создать класс Person содержащий поля имя, фамилия, возраст
3. Сгенерировать список из 100 экземпляров класса Person
[Person(‘Alex’, ‘Smith’, 23), Person(‘Bob’, ‘Alan’, 44)…]
4. Найти самого старшего и самого младшего человека из списка. Вывести результат на экран.
"""
import random

FIRST_NAMES = 'names.txt'
LAST_NAMES = 'lastnames.txt'
AGE_LIMITS = [18, 80]


class Person:

    def __init__(self, name=None, lastname=None, age=None):
        self.name = name
        self.lastname = lastname
        self.age = age
        if not all((name, lastname, age)):
            self.name, self.lastname, self.age = self.person_generator().__next__()

    @staticmethod
    def person_generator(name=None, lastname=None, age=None):
        if not name:
            with open(FIRST_NAMES, 'r') as file:
                name = random.choice([each.strip() for each in file.read().split(',')])
        if not lastname:
            with open(LAST_NAMES, 'r') as file:
                lastname = random.choice([each.strip() for each in file.read().split(',')])
        if not age:
            age = random.randint(AGE_LIMITS[0], AGE_LIMITS[1])
        yield [name, lastname, int(age)]


if __name__ == '__main__':
    # 1 - задание по функции-генератору - на основе статического метода класса Person
    for i in Person.person_generator():
        print(i)

    # 2 - находим самого старшего / младшего из случайно сгенерированной группы из 100 человек
    group = []
    for i in range(100):
        group.append(Person())
    max_age = group[0].age
    min_age = group[0].age
    for employee in group:
        if max_age < employee.age:
            max_age = employee.age
            max_age_person = employee
        if min_age > employee.age:
            min_age = employee.age
            min_age_person = employee
    print(
        f'{max_age_person.name} {max_age_person.lastname} - cамый старший из группы. Его возраст: {max_age_person.age}',
        f'{min_age_person.name} {min_age_person.lastname} - cамый младший из группы. Его возраст: {min_age_person.age}',
        sep='\n'
    )
