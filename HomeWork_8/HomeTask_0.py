"""
Дописать конвертер!
Дoлжен перехватывать все возможные ошибки, работать в цикле.
"""
rates = {
    'UAH' : 1,
    'USD' : 26,
    'EUR' : 31,
    'FNT' : 35
}


class Exchanger:
    def __init__(self, base_currency='', output_currency='', money=''):
        self.base_currency = base_currency
        self.output_currency = output_currency
        self.money = money

    def conversion(self):
        try:
            self.money = float(self.money)
        except ValueError:
            return 'Вы неверно задали сумму для конвертации'
        try:
            pre_result = float(self.money) * rates.get(self.base_currency.upper())
        except TypeError:
            return 'Вы неверно задали начальную валюту'
        try:
            result = pre_result / rates.get(self.output_currency.upper())
        except TypeError:
            return 'Вы неверно задали конечную валюту'
        return round(result, 2)

    def exchange_success(self):
        if isinstance(self.conversion(), float):
            return True
        return False

    def __str__(self):
        output = [
            f'Начальная валюта: {self.money} {self.base_currency.upper()}',
            f'Результат конвертации: {self.conversion()} {self.output_currency.upper()}'
        ]
        return '***\n' + '\n'.join(output)


def exchange():
    exchange_operation1 = Exchanger()
    while not exchange_operation1.exchange_success():
        exchange_operation1.base_currency = input('C какой валюты произвести конвертацию? (USD | UAH | EUR | FNT): ')
        exchange_operation1.money = input('Какую сумму Вы хотите конвертировать? ')
        exchange_operation1.output_currency = input('В какую валюту произвести конвертацию? (USD | UAH | EUR | FNT): ')
        print(exchange_operation1)


if __name__ == '__main__':
     exchange()
