"""
Переводчик на солёный язык.
Правило: после каждой гласной вставляем с + сама гласная.
ПРИМЕР
Привет -> Приcивеcет
Сальса -> саcальсаcа
"""
vowels = ['а', 'о', 'и', 'й', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
test_data = 'Привет, Сальса, Покемон'


def salty_transform(some_phrase: str):
    salty_phrase = []
    for i in range(len(some_phrase)):
        salty_phrase.append(some_phrase[i].lower())
        for j in range(len(vowels)):
            if some_phrase[i].lower() == vowels[j]:
                salty_phrase.append('с' + some_phrase[i])
    return ''.join(salty_phrase)


if __name__ == '__main__':
    user_phrase = input('Введите слово или фразу, которую хотите подсолить: ')

    if not user_phrase:
        user_phrase = test_data

    print(salty_transform(user_phrase))

