'''
Дано двузначное число.
Определить:
1. входит ли в запись этого числа цифра 3
2. входит ли в запись этого числа цифра а
'''

input_double_digit = float(input('Введите произвольное двузначное число: '))
a = float(input('Введите значение для числа а: '))

# проверяем 1-е условие
if (input_double_digit // 10) == 3 and (input_double_digit % 10) != 3:
    print('цифра 3 входит в заданное двузначное число слева')
elif (input_double_digit % 10) == 3 and (input_double_digit // 10) != 3:
    print('цифра 3 входит в заданное двузначное число справа')
elif (input_double_digit // 10) == 3 and (input_double_digit % 10) == 3:
    print('цифра 3 входит в заданное двузначное число слева и справа')
else:
    print('цифра 3 не входит в заданное двузначное число')

# проверяем 2-е условие
if a >= 10 and input_double_digit == a:
    print('цифра a равняется заданному двузначному числу')
elif (input_double_digit // 10) == a and (input_double_digit % 10) != a:
    print('цифра a входит в заданное двузначное число слева')
elif (input_double_digit % 10) == a and (input_double_digit // 10) != a:
    print('цифра a входит в заданное двузначное число справа')
elif (input_double_digit // 10) == a and (input_double_digit % 10) == a:
    print('цифра a входит в заданное двузначное число слева и справа')
else:
    print('цифра a не входит в заданное двузначное число')