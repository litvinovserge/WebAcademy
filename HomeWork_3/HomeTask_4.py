'''
Вывести на экран 10 первых простых чисел используя функцию задания 1
'''

def is_prime(a):
    a = abs(int(a))
    checker = 0
    if a == 2:
        return True
    elif a % 2 == 0:
        return False
    else:
        for i in range(3, a + 1):
            if a % i == 0:
                checker = checker + 1
        if checker >= 2:
            return False
        else:
            return True

# начало основной программы
j = 1
for i in range(1, 500):
    if is_prime(i):
        print(i)
        j += 1
    if j > 10:
        break



