"""
Опишите класс Сотрудника, который включает такие поля как имя, фамилия, отдел, год поступления на работу.
Конструктор должен генерировать исключение в случай неправильных данных
(Например если имя состоит из 1 символа или его длинна больше 30 символов, год поступления на работу меньше,
чем год создания компании и т.д.)

"""
from datetime import *


class EmployeeError(ValueError):

    def __init__(self, *messages):
        self.message = messages


class Employee:

    __DEPARTMENTS = ['Manager', 'Programmer', 'CEO']

    # custom exceptions для аргументов класса Employee - name, surname
    def __name_ruler(self):
        if not self.name.isalpha() or not self.surname.isalpha():
           EmployeeError.message = 'Имя и Фамилия могут содержать только буквы.'
           raise EmployeeError
        elif len(self.name) < 1 or len(self.surname) < 1:
            EmployeeError.message = 'Имя и Фамилия должны содержать более 1го символа.'
            raise EmployeeError
        elif len(self.name) > 30 or len(self.surname) > 30:
            EmployeeError.message = 'Имя и Фамилия не могут быть более 30 символов.'
            raise EmployeeError

    # custom exceptions для аргументов класса Employee - year_of_hiring
    def __year_ruler(self):
        if not self.year_of_hiring.isdigit():
            EmployeeError.message = 'Год может сожержать только цифры.'
            raise EmployeeError
        elif int(self.year_of_hiring) > datetime.today().year:
            EmployeeError.message = 'Год принятия на работу не может превышать текущий.'
            raise EmployeeError
        elif int(self.year_of_hiring) < 2010:
            EmployeeError.message = 'Эй, наша компания создана в 2010! Не можем нанять сотрудника задним числом.'
            raise EmployeeError

    # custom exceptions для аргументов класса Employee - department
    def __department_ruler(self):
        if self.department not in self.__DEPARTMENTS:
            EmployeeError.message = 'Oops, у нас такого департамента пока нет ;-( . Выбирай из: ' + \
                                     ' | '.join(self.__DEPARTMENTS)
            raise EmployeeError

    def __init__(self, name="", surname="", department="", year_of_hiring=""):
        self.name = name
        self.surname = surname
        self.department = department
        self.year_of_hiring = year_of_hiring

        # проводим текст на ошибки сразу после инициализации экземляра класса Employee
        try:
            self.__name_ruler()
        except EmployeeError:
            print(f'{EmployeeError.__name__} : {EmployeeError.message}')
        try:
            self.__department_ruler()
        except EmployeeError:
            print(f'{EmployeeError.__name__} : {EmployeeError.message}')
        try:
            self.__year_ruler()
        except EmployeeError:
            print(f'{EmployeeError.__name__} : {EmployeeError.message}')


if __name__ == '__main__':
    # генерируем ошибки
    print('Пробуем создать работника со следующими данными: (Vasya1, Pupkin, CEO2, 2019)\n***')
    employee1 = Employee('1Vasya', 'Pupkin', 'CEO2', '2019')
    print('***')

    # вводим безошибочные данные
    print('Пробуем создать работника со следующими данными: (Petya, Vasiliev, CEO, 2011)\n***')
    employee2 = Employee('Petya', 'Vasiliev', 'CEO', '2011')
