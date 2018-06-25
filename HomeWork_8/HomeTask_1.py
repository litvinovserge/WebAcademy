"""
Напишите программу калькулятор, реализующую операции (+ - * /).
Программа выдает сообщение в случай некорректных данных и продолжает работу.
"""


class CalcError(Exception):

    def __init__(self, message='Other CalcError'):
        self.message = message


class Calculator:
    __MY_OPERATIONS = ['+', '-', '*', '\ ']

    def __init__(self):
        pass

    def __input_analyzer(self, some_input):
        analyzer = []

        for symbol in some_input.split(' '):
            if symbol != '':
                analyzer.append(symbol)

        # проверяем введены ли допустимые мат. операции
        counter = 0
        for item in analyzer:
            if item in self.__MY_OPERATIONS:
                counter += 1
        if counter <= 0:
            CalcError.message = ''.join(['Введенные мат. операции не поддерживаются! Пробуйте следующие: ',
                                         ' , '.join(self.__MY_OPERATIONS), 'Вводите их через пробел после числа.'
                                         ])
            raise CalcError
        if counter > 1:
            CalcError.message = ''.join(['Вы ввели несколько операций! Калькулятор работает со следующими операциями:',
                                         ' , '.join(self.__MY_OPERATIONS), 'Вводите их через пробел после числа.'
                                         ])
            raise CalcError

        # проверяем наличие цифр
        counter = 0
        for item in analyzer:
            if item not in self.__MY_OPERATIONS and item.isdigit():
                counter += 1
        if len(analyzer) > 3:
            CalcError.message = 'Неверный ввод данных! Вводите данные в формате: ЧИСЛО_МАТ.ОПЕРАЦИЯ_ЧИСЛО'
            raise CalcError
        elif counter <= 0:
            CalcError.message = 'Вы не ввели чисел. Это всё-таки калькулятор.'
            raise CalcError
        elif counter == 1:
            CalcError.message = 'Вы ввели лишь одно число, нужно два. Числа от мат.операции должны отделяться пробелом.'
            raise CalcError
        elif counter > 2:
            CalcError.message = 'Этот калькулятор работает лишь с двумя числами =( ' + \
                                'Ждите обновленную версию калькулятора =)'
            raise CalcError
        return ' '.join(analyzer)

    def calculation(self, some_data):
        try:
            return eval(self.__input_analyzer(some_data))
        except CalcError:
            print(CalcError.message)


if __name__ == '__main__':
    calc = Calculator()
    user_input = ''
    while user_input.lower() != 'exit':
        user_input = input(('*** CALCULATOR ***\nДля выхода из калькулятора введите exit\nСтрока ввода: '))
        print(calc.calculation(user_input))
