'''
Написать функцию is_prime(a), которая принимает число и возвращает True или False
в зависимости от того, простое это число или нет
'''

def is_prime(a):
    a = abs(int(a))
    checker = 0
    if a == 2:
        print('Число', a, 'является простым')
        return True
    elif a % 2 == 0:
        print('Число', a, 'является сложным')
        return False
    else:
        for i in range (3, a + 1):
            if a % i == 0:
                checker = checker + 1
                return False
        if checker >= 2:
            print('Число', a, 'является сложным')
            return False
        else:
            print('Число', a, 'является простым')
            return True

# начало основной программы
user_number = input('Введите любое число: ')
print(is_prime(user_number))
