"""
Написать программу запрашивающую у пользователя его имя при первом запуске.
При последующих запусках программа должна обращаться по имени.
Хранить имя последнего юзера в файле.

Пример
- Первый запуск:
Привет! Введи свое имя!
>>Алексей
Привет, Алексей!
1. Закрыть программу
2. Сменить имя.
- Последующие запуски:
Привет, Алексей!
1. Закрыть программу
2. Сменить имя.
"""
import os.path

LOCAL_BASE = 'dummy.txt'


def user_name_writer(filename):
    with open(filename, 'w') as file:
        user_name = input('Привет! Как тебя зовут?\n')
        file.write(user_name)


if __name__ == '__main__':
    if not os.path.isfile(LOCAL_BASE):
        user_name_writer(LOCAL_BASE)
    elif not os.path.getsize(LOCAL_BASE):
        user_name_writer(LOCAL_BASE)
    else:
        with open(LOCAL_BASE) as file:
            print(f'Привет, {file.read()}!\n1. Закрыть программу\n2. Сменить имя')
            user_options = ''
            while user_options not in ['1', '2']:
                user_options = input()
                if user_options == '2':
                    user_name_writer(LOCAL_BASE)


