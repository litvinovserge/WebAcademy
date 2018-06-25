"""
Опишите класс Сотрудника, который включает такие поля как имя, фамилия, отдел, год поступления на работу.
Конструктор должен генерировать исключение в случай неправильных данных
(Например если имя состоит из 1 символа или его длинна больше 30 символов, год поступления на работу меньше,
чем год создания компании и т.д.)

"""
from datetime import *


class EmployeeErrors(ValueError):

    def __init__(self, *messages):
        self.message = messages


class Employee:

    __DEPARTMENTS = ['Manager', 'Programmer', 'CEO']

    def __name_ruler(self):
        if not self.name.isalpha() or not self.surname.isalpha():
           EmployeeErrors.message = 'Имя и Фамилия могут содержать только буквы'
           raise EmployeeErrors
        elif len(self.name) < 1 or len(self.surname) < 1:
            EmployeeErrors.message = 'Имя и Фамилия должны содержать более 1го символа'
            raise EmployeeErrors
        elif len(self.name) > 30 or len(self.surname) > 30:
            EmployeeErrors.message = 'Имя и Фамилия не могут быть более 30 символов'
            raise EmployeeErrors

    def __year_ruler(self):
        if not self.year_of_hiring.isdigit():
            EmployeeErrors.message = 'Год может сожержать только цифры'
            raise EmployeeErrors
        elif int(self.year_of_hiring) > datetime.today().year:
            EmployeeErrors.message = 'Год принятия на работу не может превышать текущий'
            raise EmployeeErrors
        elif int(self.year_of_hiring) < 2010:
            EmployeeErrors.message = 'Эй! Наша компания создана в 2010'
            raise EmployeeErrors

    def __department_ruler(self):
        if self.department not in self.__DEPARTMENTS:
            EmployeeErrors.message = 'OOPS, у нас такого департамента пока нет! Выбирай из: ' + \
                                     ' | '.join(self.__DEPARTMENTS)
            raise EmployeeErrors

    def __init__(self, name="", surname="", department="", year_of_hiring=""):
        self.name = name
        self.surname = surname
        self.department = department
        self.year_of_hiring = year_of_hiring

        # проводим текст на ошибки сразу после инициализации экземляра класса Employee
        try:
            self.__name_ruler()
        except EmployeeErrors:
            print(EmployeeErrors.message)
        try:
            self.__department_ruler()
        except EmployeeErrors:
            print(EmployeeErrors.message)
        try:
            self.__year_ruler()
        except EmployeeErrors:
            print(EmployeeErrors.message)


if __name__ == '__main__':
    # генерируем ошибки
    print('Пробуем создать работника со следующими данными: (Vasya1, Pupkin, CEO2, 2019)\n***')
    employee1 = Employee('1Vasya', 'Pupkin', 'CEO2', '2019')
    print('***')

    # вводим безошибочные данные
    print('Пробуем создать работника со следующими данными: (Petya, Vasiliev, CEO, 2011)\n***')
    employee2 = Employee('Petya', 'Vasiliev', 'CEO', '2011')
