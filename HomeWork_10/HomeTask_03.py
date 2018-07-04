"""
Определите размер файла имя которого вводи пользователь.
Выведите его на экран - в байтах, мегабайтах, гигабайтах.
"""


if __name__ == '__main__':
    target_file = input('Введите путь к файлу: ')
    with open(target_file, 'rb') as file_source:
        size_bytes = len(file_source.read())
        size_mb = size_bytes / 2 ** 20
        size_gb = size_bytes / 2 ** 30
    print(f'Размер файла в байтах: {size_bytes}\n'
          f'Размер файла в Мегабайтах: {size_mb}\n'
          f'Размер файла в Гигабайтах: {size_gb}'
    )
