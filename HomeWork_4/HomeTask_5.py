"""
Посчитать сумму первых двух четных чисел в списке
[5, 7, 8, 3, 4, 6, 8] -> 12
"""

def my_func(input_list):
    counter = 0
    my_sum = 0
    for i in range(len(input_list)):
        if counter >= 2:
            return my_sum
        elif input_list[i] % 2 == 0:
            my_sum += input_list[i]
            counter += 1

if __name__ == '__main__':
    s_data = [1, 2, 3, 4, 5, 6, 7, 8]
    print('Cумма первых двух четных элементов списка', s_data, 'равна =', my_func(s_data))
