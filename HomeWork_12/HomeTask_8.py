"""
Есть код:
class User:
def __init__(self, username, password, role):
self.username = username
self.password = password
self.role = role
def show_panel(user: User):
print('Hello', user.username)
print('Here is your panel!')

1. Написать декоратор allow_admin, который допускает только юзеров с role
= 'admin'
Если юзер не админ, выводить 'Panel is not permitted'.
Пример:
@allow_admin
def show_panel(user: User):
print('Hello', user.username)
print('Here is your panel!')
>>user = User('eliasmir', '111', 'admin')
>>show_panel(user)
Hello eliasmir
Here is your panel!
>>user = User('vanrossum', 'pep8', 'user')
>>show_panel(user)
Panel is not permitted

2. Написать декоратор для функции show_panel позволяющий выбрать роли
которые допускаются.
@allow(roles=['admin', 'root', 'owner'])
def show_panel(user: User):
print('Hello', user.username)
print('Here is your panel!')
>>user = User('vanrossum', 'pep8', 'owner')
>>show_panel(user)
Hello eliasmir
Here is your panel!
"""


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return '/'.join([self.username, self.password, self.role])


# декоратор для задания - 1
def allow_admin(some_function):

    def wrapper(*args, **kwargs):
        if args[0].role == 'admin':
            some_function(*args, **kwargs)
        else:
            print('Panel is not permitted! Get OUT!\n***')

    return wrapper


# декоратор для задания - 2
def allow_admin_2(dec_args):

    def decorator(some_function):

        def wrapper(*args, **kwargs):
            # я не понял зачем нам аргументы в декораторе? как передать понятно, но само задание 8.2 непонимаию
            # не понял в чем функциональная разница задания 8.1 от 8.2
            print(dec_args)

        return wrapper

    return decorator


@allow_admin
def show_panel(user: User):
    print('Hello', user.username)
    print('Here is your panel!\n***')


@allow_admin_2(['admin', 'root', 'owner'])
def show_panel_2(user: User):
    print('Hello', user.username)
    print('Here is your panel!\n***')


if __name__ == '__main__':

    # тестируем декоратор для задания - 1
    tester1 = User('Sergey', '123', 'admin')
    tester2 = User('Vasya', '321', 'user')
    print('Инициализируем двух пользователей\n{} и {}\n***'.format(f'tester1: {tester1}', f'tester2: {tester2}'))
    print('Результат выполнения функции show_panel для пользователя tester1')
    show_panel(tester1)
    print('Результат выполнения функции show_panel для пользователя tester2')
    show_panel(tester2)
