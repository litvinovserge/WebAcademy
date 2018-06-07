'''
Написать функцию, которая выводит на экран n первых четных чисел.
'''

def even_finder(user_number):
    user_number = abs(int(user_number))
    j = 0
    for i in range(1, 3 * user_number):
        if i % 2 == 0:
            print(i)
            j += 1
        if j >= user_number:
            break

# начало основной программы
n = input('Какое кол-во четных чисел вы хотите увидеть?')
even_finder(n)