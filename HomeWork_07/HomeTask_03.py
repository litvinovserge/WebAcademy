"""
1. Описать класс Книга. (год, название, автор)
2. Описать метод __eq__  для сравнения
~~~
 ПРИМЕР
 book1 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
 book2 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
 book3 = Book(‘Над пропастью во ржи’, 1951, ‘Jerome David Salinger’)

 book1 == book2
 True
 book1 == book3
 False
~~~
3. Добавить поле с отзывами и методы добавить отзыв, посмотреть все отзывы.
~~~
 ПРИМЕР
 book1.add_review(‘Cool!!’)
 book1.add_review(‘Not bad’)
 book1.show_reviews()
 1.
 Cool!!
 2.
 Not bad
"""


class Book:

    def __init__(self, title=None, author=None, year=None):
        self.title = title
        self.author = author
        self.year = year
        self.reviews = []

    def add_review(self, new_review):
        if isinstance(new_review, list):
            for review in new_review:
                self.reviews.append(review)
        elif isinstance(new_review, str):
            self.reviews.append(new_review)

    def show_reviews(self):
        if self.reviews:
            print('Для книги:', self.title, 'автора:', self.author, 'издательства:', self.year, '\n'
                  'Было найдено', len(self.reviews), 'отзывов', '\n'
                  '******'
                  )
            for review in range(len(self.reviews)):
                print(review + 1, '-', self.reviews[review] )
        else:
            print('Для книги:', self.title, 'автора:', self.author, 'издательства:', self.year, '\n'
                'Отзывов не найдено')

    def __eq__(self, other_object):
        if self.title == other_object.title and self.author == other_object.author and self.year == other_object.year:
            return True
        else:
            return False

    def __str__(self):
        all_data = [self.title, self.author, str(self.year)]
        return ' || '.join(all_data)

if __name__ == '__main__':

    # 0 инициализация начальных данных
    book1 = Book('Nineteen Eighty-Four', 'George Orwell', 1949)
    book2 = Book('Nineteen Eighty-Four', 'George Orwell', 1949)
    book3 = Book('Над пропастью во ржи', 'Jerome David Salinger', 1951)
    print('0. заполняем нашу библиотеку книгами book1, book2, book3',
          'book1: ' + str(book1), 'book2: ' + str(book2), 'book3: ' + str(book3), sep='\n'
          )

    # 1. проверка метода __eq__  для сравнения экземпляров объекта Books
    print( '1. проверка метода __eq__  для сравнения экземпляров объекта Books', '\n'
           '- сравним книгу book1:', book1, 'и книгу book2:', book2, '\n'
           'результат сравнения:', book1 == book2, '\n'
           '- сравним книгу book2:', book2, 'и книгу book3:', book3, '\n'
           'результат сравнения:', book2 == book3
          )

    # 2. тест метода для добавления отзывов / отображения всех отзывов
    print('2. проверим добавление и отображение отзывов для книг. '
          'Ниже выведем результат добавления отзывов для книги book1')
    book1.add_review('Лучшая книга!')
    book1.add_review('Она поменяла мою жизнь! Жизнь стала хуже, ура!')
    book1.show_reviews()

