"""
Написать программу способную регистрировать пользователей, добавить функциональность регистрации, входа и выхода.
Каждый последующий запуск программы должен восстанавливать предыдущее состояние.
(если авторизован юзер Илья, то при перезапуске программа должна поприветствовать Илью).
Пользователей может быть несколько, отлавливать ситуации когда пароль введен неверно или когда нет такого юзера.
Для сохранения состояния можно использовать модуль pickle или json. Один из вариантов хранения данных
(словарь где ключей выступает логин, а значением словарь с информацией про пользователя).
Такую структуру легко хранить в jsone:
users = {
   ‘eliasmir’: {‘name’: ‘Илья’, ‘login’: ‘eliasmir’, ‘password’: ‘qwerty’},
   ‘Kate134’: {‘name’: ‘екатерина’,  ‘login’: ‘Kate134’, ‘password’: ‘kt123’},
}

Пример (регистрация):
Привет!
1. Регистрация
2. Вход
3. Выход
>>1
Введите имя:
>>Илья
Введите логин:
>>eliasmir
Введите пароль:
>>qwerty
Привет, Илья!
1. Регистрация
2. Вход
3. Выход

Пример (Выход):
Привет, Илья!
1. Регистрация
2. Вход
3. Выход
>>3
Пока, Илья!
Привет!
1. Регистрация
2. Вход
3. Выход

Пример (Вход):
Привет!
1. Регистрация
2. Вход
3. Выход
>>2
Логин:
>>eliasmir
Пароль:
>>qwerty
Привет, Илья!
1. Регистрация
2. Вход
3. Выход
"""
import os.path
import json


class UserForm:
    """
    Class Формы авторизации для пользователей
    Структура хранения данных - json
    Формат временных файлов - txt
    """
    LOCAL_BASE = 'localbase.json'
    TEMP_FILE = 'temp.txt'

    def __init__(self):
        self.database_check()  # проверяем существует ли файл с базой данных, если его нет - создаем пустой
        with open(self.TEMP_FILE) as file:
            self.last_state = file.read()

    # проверка наличия файла базы данных
    def database_check(self):
        if not os.path.isfile(self.LOCAL_BASE):
            with open(self.LOCAL_BASE, 'w') as file:
                json.dump([], file)
        if not os.path.isfile(self.TEMP_FILE):
            with open(self.TEMP_FILE, 'w') as file:
                pass

    # обработка выбора пользователя
    def choice_handler(self):
        if self.user_choice == '1':
            self.registration()
        elif self.user_choice == '2':
            self.authorization()
        elif self.user_choice == '3':
            self.exit()

    # 0 - стартовое окно формы
    def init_page(self):
        print(f'Привет{self.last_state}!\n1. Регистрация\n2. Вход\n3. Выход')
        self.user_choice = ''
        while self.user_choice not in ['1', '2', '3']:
            self.user_choice = input()
        self.choice_handler()

    # 1 - регистрация пользователей
    def registration(self):
        user_name = input('Введите ваше имя: ')
        user_login = input('Введите login: ')
        while self.check_duplicate_login(user_login):
            print('Такой login уже есть в базе, попробуйте другой!')
            user_login = input('Введите login: ')
        user_password = input('Введите password: ')
        database_unit = {
            'user_name': user_name,
            'user_login': user_login,
            'user_password': user_password
        }
        with open(self.LOCAL_BASE) as file:
            buffer = json.load(file)
        buffer.append(database_unit)
        with open(self.LOCAL_BASE, 'w') as file:
            json.dump(buffer, file)
        print(f'Поздравляем, {user_name}! Теперь Вы можете пройти процесс авторизации в нашей системе!')

    # 2 - авторизация пользователей
    def authorization(self):
        user_login = input('Введите login: ')
        user_password = input('Введите password: ')
        with open(self.LOCAL_BASE) as file:
            buffer = json.load(file)
        all_names = [buffer[user].get('user_name') for user in range(len(buffer))]
        all_logins = [buffer[user].get('user_login') for user in range(len(buffer))]
        all_passwords = [buffer[user].get('user_password') for user in range(len(buffer))]
        if user_login not in all_logins:
            print('Такого пользователя нет в базе!\nПройдите процесс регистрации, или введите другой login!')
        else:
            index = all_logins.index(user_login)
            attempts = 3
            while attempts > 0:
                if user_password != all_passwords[index]:
                    print(f'Неверный пароль! Осталось попыток: {attempts}')
                    user_password = input('Введите password: ')
                    attempts -= 1
                else:
                    print(f'Привет, {all_names[index]}! Выполнена успешная авторизация!')
                    with open(self.TEMP_FILE, 'w') as file_source:
                        file_source.write(', ' + all_names[index])
                    break
            else:
                print('У Вас закончились попытки ввода пароля')

    # 3 - выход пользователя
    def exit(self):
        print('Жаль ;-( А ведь для авторизованных пользовалетей сегодня мы приготовили кое-что потрясающее!')
        with open(self.TEMP_FILE, 'w') as file_source:
            pass

    # дополнения - проверка на дубликат user_login
    def check_duplicate_login(self, user_login):
        with open(self.LOCAL_BASE) as file:
            buffer = json.load(file)
        all_logins = [buffer[user].get('user_name') for user in range(len(buffer))]
        if user_login in all_logins:
            return True


if __name__ == '__main__':
    UserForm().init_page()



