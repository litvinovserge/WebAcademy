"""
Создать класс Автосалон содержащий информацию: адрес, имя, список доступных машин.
Реализовать методы для:
1. отображения всех доступных машин
2. добавления новых машин
3. покупки машин (после покупки машина удаляется из списка)
4. проверки на наличие такой машины в салоне
"""


class AutoSalon:

    def __init__(self, name=None, address=None, available_cars=[]):
            self.name = name
            self.address = address
            self.available_cars = available_cars[:]

    def addcar(self, new_cars):
        if isinstance(new_cars, list):
            for car in new_cars:
                self.available_cars.append(car)
        elif isinstance(new_cars, str):
            self.available_cars.append(new_cars)

    def buycar(self, buyed_cars):
        if isinstance(buyed_cars, list):
            buffer = self.available_cars[:]
            for car_in_salon in buffer:
                for car_2_buy in buyed_cars:
                    if car_in_salon == car_2_buy:
                        self.available_cars.remove(car_in_salon)
        elif isinstance(buyed_cars, str):
            self.available_cars.remove(buyed_cars)


    def check_availability(self, check_car):
        for car in self.available_cars:
            if car == check_car:
                print('Такая машина есть в салоне', self.name, 'Находящийся по адресу', self.address)
                exit()
        print('Такого автомобиля в салоне нет')


    def show_info(self):
        print(self)

    def __str__(self):
        salon_info = [
                      'Название салона: ' + self.name,
                      'Адрес салона: ' + self.address,
                      'Доступные автомобили: ' + ' | '.join(self.available_cars)
                     ]
        return '\n'.join(salon_info)


if __name__ == '__main__':

    # 0. инициализация начальных данных с выводом информации на экран
    cars_in_salon1 = ['Audi', 'Bmw', 'VW']
    salon1 = AutoSalon('BestAuto', 'ABC street, 12', cars_in_salon1)
    salon1.show_info()

    # 1. отображение всех доступных машин
    print('1. отображения всех доступных машин: ', salon1.available_cars)

    # 2. добавление новых машин
    salon1.addcar(['Bentley', 'Ferrari', 'Mazeratti'])
    print('2. добавление новых машин: ', salon1.available_cars)

    # 3. покупка машин
    salon1.buycar(['Bentley', 'Ferrari', 'Mazeratti'])
    print('3. покупка машин: ', salon1.available_cars)

    # 4. проверка на наличие машины в салоне
    print('4.1 проверка на наличие машины Renault в салоне: ')
    salon1.check_availability('Renault')
    print('4.2 проверка на наличие машины Bmw в салоне: ')
    salon1.check_availability('Bmw')

