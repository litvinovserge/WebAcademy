"""
Дан список чисел, заменить каждое число на квадрат этого числа.
[1, 2, 3, 4] -> [1, 4, 9, 16]
"""

if __name__ == '__main__':
    s_data = [1, 2, 3, 4]
    for i in range(len(s_data)):
        s_data[i] *= s_data[i]
    print(s_data)

