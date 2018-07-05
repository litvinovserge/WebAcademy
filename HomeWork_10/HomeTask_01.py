"""
Переписать информацию с одного файла в другой.
"""
TARGET_FILE = 'HomeTask_01_file'
EXTENSION = '.txt'


if __name__ == '__main__':
    with open(TARGET_FILE + EXTENSION) as file:
        buffer = file.read()
    with open(TARGET_FILE + 'copy' + EXTENSION, 'w') as file_copy:
        file_copy.write(buffer)
