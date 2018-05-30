'''
Задача №4
Программа запрашивает у пользователя строку и выводит ее по центру в таблице 20х3.
'''
TABLE_SYMBOL = '*' #задаем символ обрамления рамки

user_data = input('Введите строку длиной до 20 символов: ')

ramka = TABLE_SYMBOL * 20
leng_central_string  = int((20 - 2 - len(user_data))/2) #при нечетном кол-ве символов получим смещение основной строки на 1 влево, без условных операторов нормально не сделать
central_string = TABLE_SYMBOL + ' ' * leng_central_string + user_data  + ' ' * leng_central_string + TABLE_SYMBOL

print(ramka,central_string,ramka,sep='\n')