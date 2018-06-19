"""
Создать класс автомобиль, который содержит информацию о автомобилях
Описать метод __str__
ПРИМЕР
"""


class Car:

    def __init__(self, model=None, color=None, year=None, price=None):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        car_info = [
                    'model: ' + self.model,
                    'color: ' + self.color,
                    'year: ' + str(self.year),
                    'price: ' + str(self.price),
                    ]
        return '\n'.join(car_info)


if __name__ == '__main__':
    Audi = Car('Audi', 'Black', '2018', '35 000$')
    VW = Car('VW', 'Grey', '2015', '15 000$')
    Opel = Car('Opel', 'Yellow', '2013', '13 500$')
    print(Audi, VW, Opel, sep='\n***\n')