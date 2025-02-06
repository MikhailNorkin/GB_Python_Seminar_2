'''
Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять не менее 42 знаков после запятой.
'''

from math import pi
import decimal

def main():
    diameter = int(input('Введите диаметр круга '))
    decimal.getcontext().prec = 42
    print('Длина круга будет равна ', decimal.Decimal(diameter * pi))
    print('Площадь круга равна ', decimal.Decimal(pi * diameter**2 / 4))

if __name__ == "__main__":
    main()

