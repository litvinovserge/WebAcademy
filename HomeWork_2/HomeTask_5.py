'''
Напишите программу, запрашивающую Имя, Фамилию, Отчество и номер группы студента и выводящую введённые данные
в следующем виде:
 ************************************
 *Лабораторная работа № 1   *
 *Выполнил(а): ст. гр. ЗИ-123 *
 *Иванов Андрей Петрович    *
 ************************************
Необходимо, чтобы программа сама определяла нужную длину рамки. Сама же длина рамки зависит от длины наибольшей
строки внутри рамки. Используя циклы for легко можно выровнять стороны рамки.
'''
TABLE_SYMBOL = '*'

user_1st_name = input('Введите Ваше Имя: ')
if not user_1st_name:
    user_1st_name = 'Сергей'
user_2nd_name = input('Введите Вашу Фамилию: ')
if not user_2nd_name:
    user_2nd_name = 'Литвинов'
user_3rd_name = input('Введите Вашe Отчество: ')
if not user_3rd_name:
    user_3rd_name = 'Викторович'
user_class_number = input('Введите номер Вашей группы: ')
if not user_class_number:
    user_class_number = '777'

user_full_name = user_2nd_name + ' ' + user_1st_name + ' ' + user_3rd_name

table_lab = TABLE_SYMBOL + 'Лабораторная работа № 1' + TABLE_SYMBOL
table_group = TABLE_SYMBOL + 'Выполнил(а): ст. гр. ' + user_class_number + TABLE_SYMBOL
table_student = TABLE_SYMBOL + user_full_name + TABLE_SYMBOL

if len(table_lab) > len(table_group) and len(table_lab) > len(table_student):
    space_length = len(table_lab)
elif len(table_group) > len(table_lab) and len(table_group) > len(table_student):
    space_length = len(table_group)
else:
    space_length = len(table_student)

table_format_left = TABLE_SYMBOL + ' ' * space_length
table_format_right = ' ' * space_length + TABLE_SYMBOL

table_frame = TABLE_SYMBOL * space_length
table_lab = TABLE_SYMBOL + ' ' * ((space_length - len(table_lab) - 1) // 2) + 'Лабораторная работа № 1' + ' ' * ((space_length - len(table_lab) - 1) // 2) + TABLE_SYMBOL
table_group = TABLE_SYMBOL + ' ' * ((space_length - len(table_group) - 1) // 2) + 'Выполнил(а): ст. гр. ' + user_class_number + ' ' * ((space_length - len(table_group) - 1) // 2) + TABLE_SYMBOL
table_student = TABLE_SYMBOL + ' ' * ((space_length - len(user_full_name) - 1) // 2) + user_full_name + ' ' * ((space_length - len(user_full_name) - 1) // 2) + TABLE_SYMBOL

print(table_frame, table_lab, table_group, table_student, table_frame, sep='\n')
