"""
Дан список строк. Посчитать количество символов в первой строке где есть символ ‘а’.
[‘‪fur’, ‘skin’, ‘coat’, ‘pelage’, ‘jack‬’] -> 4 # len(‘coat’)
"""

def find_func(input_list):
    symb = 'a'
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if input_list[i][j] == symb:
                return i, len(input_list[i])

if __name__ == '__main__':
    s_data = ['fqqqr', 'skin', 'coqqqt', 'pelage', 'jack‬']
    print('Номер индекса строки с символом ‘а’ #', find_func(s_data)[0], \
          'Количество символов в этой строке равно = ', find_func(s_data)[1])

