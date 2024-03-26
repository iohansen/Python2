"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...
  
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на 100 км" (gas_per_km)
* "пробег" (mileage)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```
должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```
выведет сообщение "проехали ... километров"
в результате поездки потратится бензин и увеличится пробег
Если топлива не хватает на указанное расстояние, едем пока хватает топлива.

г) реализовать метод: car1.info() (количество бензина в баке и пробег)
"""

class Car:
    def __init__(self):
        self.gas = 0
        self.capacity = 0
        self.gas_per_km = 0
        self.mileage = 0

    def set_initial_values(self):
        """  Устанавливаем первоначальные значения для простоты тестирования """
        self.gas = 20
        self.capacity = 120
        self.gas_per_km = 3
        self.mileage = 1500

    def fill(self, liters):
        """  Заливаем бензин в бак """
        extra_gas = liters - (self.capacity - self.gas)
        if extra_gas > 0:
            self.gas = self.capacity
            print(f'   Бак заполнен полностью')
            print(f'   В бак не вошло: {extra_gas} литров')

        else:
            self.gas = self.gas + liters

    def ride(self, kilometers):
        """  Проезжаем расстояние """
        posible_kilometers = self.gas / self.gas_per_km
        extra_kilometers = kilometers - posible_kilometers

        if posible_kilometers < kilometers:
            self.mileage = self.mileage + posible_kilometers
            self.gas = 0

            print(f'   Из требуемых {kilometers} километров смогли проехать только {posible_kilometers} километров')
            print('   К сожалению, закончился бензин')

        else:
            self.mileage = self.mileage + kilometers
            self.gas = self.gas - (self.gas_per_km * kilometers)

    def info(self):
        """  Выводим информацию о текущих параметрах """
        print(f'   Количество бензина в баке: {self.gas}')
        print(f'   Текущий пробег: {self.mileage}')


car1 = Car()

car1.set_initial_values()

print('\nПроверяем первоначальные значения:')
car1.info()

print('\nЗаливаем в бак 50 литров бензина:')
car1.fill(50)
car1.info()

print('\nПроезжаем 20 километров:')
car1.ride(20)
car1.info()

print('\nПытаемся залить в бак 200 литров бензина:')
car1.fill(200)
car1.info()

print('\nПытаемся проехать 1000 километров:')
car1.ride(1000)
car1.info()
