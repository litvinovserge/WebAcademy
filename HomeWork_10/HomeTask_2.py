"""
Скопировать файл в выбранную директорию.
Пример:
Введите путь к файлу:
>>files/avatar.jpg
Куда скопировать?
>>files2/
Готово!
"""
import os.path


if __name__ == '__main__':
    target_file = input('Введите путь к файлу: ')
    new_directory = os.path.join(input('Какая директория для сохранения ?'), os.path.basename(target_file))
    with open(target_file, 'rb') as file_source:
        with open(new_directory, 'wb') as file_copy:
            file_copy.write(file_source.read())
    print('Готово!')