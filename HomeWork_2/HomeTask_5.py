'''
Напишите программу, запрашивающую имя, фамилия, отчество и номер группы студента и выводящую введённые данные
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
user_2nd_name = input('Введите Вашe Фамилию: ')
if not user_2nd_name:
    user_2nd_name = 'Литвинов'
user_3rd_name = input('Введите Вашe Отчество: ')
if not user_3rd_name:
    user_3rd_name = 'Викторович'
user_class_number = input('Введите номер Вашей группы: ')
if not user_class_number:
    user_class_number = '777'

table_lab = TABLE_SYMBOL + 'Лабораторная работа № 1' + TABLE_SYMBOL
table_group = TABLE_SYMBOL + 'Выполнил(а): ст. гр. ' + user_class_number + TABLE_SYMBOL
table_student = TABLE_SYMBOL + user_2nd_name + ' ' + user_1st_name + ' '  + user_3rd_name + TABLE_SYMBOL

if len(table_lab) > len(table_group) and len(table_lab) > len(table_student):
    space_length = len(table_lab)
elif len(table_group) > len(table_lab) and len(table_group) > len(table_student):
    space_length = len(table_group)
else:
    space_length = len(table_student)

table_format_left = TABLE_SYMBOL + ' ' * (space_length // 2)
table_format_right = ' ' * (space_length // 2) + TABLE_SYMBOL

table_frame =  TABLE_SYMBOL * (space_length * 2)
table_lab = table_format_left + 'Лабораторная работа № 1' + table_format_right
table_group = table_format_left + 'Выполнил(а): ст. гр. ' + user_class_number + table_format_right
table_student = table_format_left + user_2nd_name + ' ' + user_1st_name + ' '  + user_3rd_name + table_format_right

print(table_frame, table_lab, table_group, table_student, table_frame, sep='\n')
