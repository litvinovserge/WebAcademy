"""
Программа конвертер валют (для валют: евро, доллар, гривна, рубль, фунт) должна переводить из любой валюты в любую.
Курсы хардкодим.
ПРИМЕР
Введите валюту: UAH
Введите сумму: 2600
В какой валюте получить результат? USD
***
2600 UAH = 100 USD
"""
currency_list = [
                    ['UAH', 1],
                    ['EUR', 30.75],
                    ['USD', 26.21],
                    ['RUB', 0.42],
                    ['FNT', 35.07]
                ]


def exchanger(base_cur, some_sum, out_cur):
    first_currency_index = 0
    second_currency_index = 0
    for i in range(len(currency_list)):
        if base_cur.upper() == currency_list[i][0]:
            first_currency_index = i
        elif out_cur.upper() == currency_list[i][0]:
            second_currency_index = i

    result = float(some_sum) * currency_list[first_currency_index][1] / currency_list[second_currency_index][1]
    return round(result, 2)


if __name__ == '__main__':
    user_1cur = input('Введите валюту (UAH, EUR, USD, RUB, FNT): ')
    user_sum = input('Введите сумму: ')
    user_2cur = input('В какой валюте выдать результат? ')

    # значения по умолчанию
    if not user_1cur:
        user_1cur = 'EUR'
    if not user_sum:
        user_sum = 100
    if not user_2cur:
        user_2cur = 'USD'

    print('*' * 10, '\n'
          'Результат конвертации:',
          user_sum, user_1cur.upper(),
          '=', exchanger(user_1cur, user_sum, user_2cur),  user_2cur.upper()
          )
