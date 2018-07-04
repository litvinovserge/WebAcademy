"""
Программа переводчик из соленого языка.
ПРИМЕР
Посокесемосон -> Покемон
"""
vowels = ['а', 'о', 'и', 'й', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
test_data = 'Приcивеcет, Cаcальсаcа, Посокесемосон!'


def anti_salty_transform(some_phrase):
    some_phrase = list(some_phrase)
    for i in range(len(some_phrase)):
        for j in range(len(vowels)):
            if some_phrase[i].lower() == vowels[j]:
                some_phrase[i + 1] = ''
                some_phrase[i + 2] = ''
    return ''.join(some_phrase)


if __name__ == '__main__':
    user_phrase = input('Введите Вашу солёную фразу или слово: ')
    if not user_phrase:
        user_phrase = test_data

    print(anti_salty_transform(user_phrase))
